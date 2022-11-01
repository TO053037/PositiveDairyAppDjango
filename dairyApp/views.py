from django.shortcuts import render, redirect
from django.http import HttpRequest, JsonResponse, Http404, HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views.decorators.http import require_POST, require_GET
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from .models import DairyContent, PictureCategory, DairyPicture
from .forms import CategoryForm, DairyPictureForm
import datetime
import json


def create_date_obj(date: str) -> datetime:
    return datetime.datetime.strptime(date, '%Y-%m-%d').date()


@login_required
def index(request: HttpRequest):
    print(request.user.email)
    context = {
        'today': datetime.date.today().strftime("%Y-%m-%d"),
    }
    print(context)
    return render(request, 'dairyApp/index.html', context)


@login_required
@require_POST
def post_dairy_content(request: HttpRequest) -> JsonResponse:
    dairy_content = {
        'content': request.POST.get('content'),
        'date': request.POST.get('date'),
        'ranking': request.POST.get('ranking'),
    }

    try:
        instance = DairyContent.objects.get(user_object=request.user,
                                            date=create_date_obj(dairy_content['date']),
                                            ranking=dairy_content['ranking'], )
        instance.content = dairy_content['content']
        instance.save()
    except DairyContent.DoesNotExist:
        DairyContent.objects.create(user_object=request.user, date=create_date_obj(dairy_content['date']),
                                    ranking=dairy_content['ranking'], content=dairy_content['content'])
    return JsonResponse({
        'dairyContent': dairy_content
    })


@login_required
@require_GET
def get_dairy_content(request: HttpRequest) -> JsonResponse:
    ranking = request.GET.get('ranking')
    date = request.GET.get('date')
    if ranking not in ['1', '2', '3']:
        return JsonResponse({
            'status': 404,
            'message': 'rankingが正しくない'
        })

    if date is None:
        return JsonResponse({
            'status': 404,
            'message': '日付が正しくない',
        })

    try:
        content = DairyContent.objects.get(user_object=request.user, ranking=ranking,
                                           date=datetime.datetime.strptime(date,
                                                                           '%Y-%m-%d').date()).content
        return JsonResponse({
            'status': 200,
            'content': content
        })
    except DairyContent.DoesNotExist:
        return JsonResponse({
            'status': 404,
        })


@login_required
@require_POST
def delete_dairy_content(request: HttpRequest) -> JsonResponse:
    try:
        instance = DairyContent.objects.get(user_object=request.user, content=request.POST.get('content'),
                                            ranking=request.POST.get('ranking'), date=request.POST.get('date'))
        instance.delete()
        return JsonResponse({
            'status': 200,
        })
    except DairyContent.DoesNotExist:
        return JsonResponse({
            'status': 404
        })


class CreateCategoryView(LoginRequiredMixin, CreateView):
    model = PictureCategory
    form_class = CategoryForm
    template_name = 'dairyApp/create_and_edit_category.html'

    def form_valid(self, form):
        instance_picture_category = form.save(commit=False)
        instance_picture_category.user_object = self.request.user
        instance_picture_category.picture_count = 0
        instance_picture_category.save()
        return HttpResponseRedirect(reverse_lazy('show_pictures'))


class EditCategoryView(LoginRequiredMixin, UpdateView):
    model = PictureCategory
    template_name = 'dairyApp/create_and_edit_category.html'
    form_class = CategoryForm

    def get_queryset(self):
        try:
            return PictureCategory.objects.filter(user_object=self.request.user, pk=self.kwargs['pk'])
        except PictureCategory.DoesNotExist:
            raise Http404('not access')

    def form_valid(self, form):
        if self.object.user_object != self.request.user:
            raise Http404('not access')
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse_lazy('show_pictures', kwargs={'category_id': self.kwargs['pk']})


class DeleteCategoryView(LoginRequiredMixin, DeleteView):
    model = PictureCategory
    template_name = 'dairyApp/delete_category.html'

    def get_queryset(self):
        try:
            return PictureCategory.objects.filter(pk=self.kwargs['pk'], user_object=self.request.user)
        except PictureCategory.DoesNotExist:
            raise Http404('not access')

    def form_valid(self, form):
        print(self.object.user_object, self.request.user)
        if self.object.user_object != self.request.user:
            raise Http404('not access')
        self.object.delete()
        return HttpResponseRedirect(reverse_lazy('show_pictures'))


class ShowPicturesView(LoginRequiredMixin, ListView):
    model = DairyPicture
    paginate_by = 50
    template_name = 'dairyApp/show_pictures.html'

    def get_queryset(self):
        try:
            category_id = self.kwargs['category_id']
            instance_category = PictureCategory.objects.get(user_object=self.request.user, pk=category_id)
            return DairyPicture.objects.filter(user_object=self.request.user,
                                               category=instance_category)
        except PictureCategory.DoesNotExist:
            raise Http404('not find')

        except KeyError:
            return DairyPicture.objects.filter(user_object=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['picture_categories'] = PictureCategory.objects.filter(user_object=self.request.user)
        return context


@login_required
def create_dairy_picture(request: HttpRequest, date: str):
    if request.method == 'POST':
        form = DairyPictureForm(request.user, request.POST, request.FILES)
        if form.is_valid():
            instance_dairy_picture = DairyPicture()
            instance_dairy_picture.title = request.POST['title']
            instance_dairy_picture.comment = request.POST['comment']
            instance_dairy_picture.image = request.FILES['image']
            instance_dairy_picture.user_object = request.user

            try:
                category_pk = request.POST['category']
                instance_dairy_picture.category = PictureCategory.objects.get(pk=category_pk,
                                                                              user_object=request.user)
                instance_picture_category = PictureCategory.objects.get(pk=category_pk, user_object=request.user)
                instance_picture_category.picture_count += 1
                instance_picture_category.save()

            except ValueError:
                instance_dairy_picture.category = None

            instance_dairy_picture.date = create_date_obj(date)
            instance_dairy_picture.save()
            return redirect('index')
    else:
        print(request.user)
        form = DairyPictureForm(user_object=request.user)
    return render(request, 'dairyApp/create_and_edit_dairy_picture.html', {'form': form})


class DeleteDairyPictureView(LoginRequiredMixin, DeleteView):
    model = DairyPicture
    template_name = 'dairyApp/delete_dairy_picture.html'

    def get_queryset(self):
        try:
            return DairyPicture.objects.filter(user_object=self.request.user, pk=self.kwargs['pk'])
        except DairyPicture.DoesNotExist:
            raise Http404('not access')

    # TODO: redirect先を前にいたページにする
    def form_valid(self, form):
        if self.request.user != self.object.user_object:
            raise Http404('not access')
        category = self.object.category
        if category is not None:
            category.picture_count -= 1
            category.save()

        self.object.delete()
        return HttpResponseRedirect(reverse_lazy('index'))


class EditDairyPictureView(LoginRequiredMixin, UpdateView):
    model = DairyPicture
    template_name = 'dairyApp/create_and_edit_dairy_picture.html'
    form_class = DairyPictureForm

    def get_queryset(self):
        try:
            return DairyPicture.objects.filter(user_object=self.request.user, pk=self.kwargs['pk'])
        except DairyPicture.DoesNotExist:
            raise Http404('not access')

    def get_form_kwargs(self):
        kwargs = super(EditDairyPictureView, self).get_form_kwargs()
        kwargs.update({'user_object': self.request.user})
        return kwargs

    def form_valid(self, form):
        if self.request.user != self.object.user_object:
            raise Http404('not access')

        if DairyPicture.objects.get(pk=self.kwargs['pk']).category != self.object.category:
            instance_category = DairyPicture.objects.get(pk=self.kwargs['pk']).category
            if instance_category is not None:
                instance_category.picture_count -= 1
                instance_category.save()
            instance_category = self.object.category
            if instance_category is not None:
                instance_category.picture_count += 1
                instance_category.save()

        self.object.save()
        return HttpResponseRedirect(reverse_lazy('index'))


@login_required
@require_GET
def get_dairy_picture(request: HttpRequest) -> JsonResponse:
    try:
        request.GET.get('date')
    except KeyError:
        raise Http404

    try:
        dairy_pictures = DairyPicture.objects.filter(user_object=request.user, date=request.GET.get('date'))
        dairy_pictures_urls = [picture.image.url for picture in dairy_pictures]
        return JsonResponse({
            'status': 200,
            'pictureUrls': dairy_pictures_urls
        })
    except DairyPicture.DoesNotExist:
        return JsonResponse({
            'status: 200',
        })

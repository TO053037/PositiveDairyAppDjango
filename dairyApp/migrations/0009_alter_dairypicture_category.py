# Generated by Django 4.1.1 on 2022-10-06 02:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dairyApp', '0008_alter_dairypicture_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dairypicture',
            name='category',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='dairyPicture', to='dairyApp.picturecategory'),
        ),
    ]

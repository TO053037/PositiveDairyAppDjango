# Generated by Django 4.1.1 on 2022-09-29 07:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dairyApp', '0002_dairypicture'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dairycontent',
            old_name='user_id',
            new_name='user_object',
        ),
        migrations.RenameField(
            model_name='dairypicture',
            old_name='user_id',
            new_name='user_object',
        ),
    ]
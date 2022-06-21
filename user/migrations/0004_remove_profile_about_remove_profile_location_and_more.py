# Generated by Django 4.0.5 on 2022-06-20 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_profile_delete_userprofile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='about',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='location',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='name',
        ),
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='nophoto.jpg', null=True, upload_to='avater/'),
        ),
    ]

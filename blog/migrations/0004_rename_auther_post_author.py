# Generated by Django 4.0.5 on 2022-06-21 08:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_post_content'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='auther',
            new_name='author',
        ),
    ]
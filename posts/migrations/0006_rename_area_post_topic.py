# Generated by Django 4.1.2 on 2022-12-01 09:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_post_area'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='area',
            new_name='topic',
        ),
    ]

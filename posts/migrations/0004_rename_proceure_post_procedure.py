# Generated by Django 4.1.2 on 2022-11-04 12:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_post_link_post_proceure'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='proceure',
            new_name='procedure',
        ),
    ]

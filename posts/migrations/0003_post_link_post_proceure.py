# Generated by Django 4.1.2 on 2022-11-03 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_post_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='link',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='post',
            name='proceure',
            field=models.TextField(blank=True),
        ),
    ]

# Generated by Django 3.0.6 on 2020-06-09 11:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recommend', '0009_movie_watch'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='watch',
        ),
    ]

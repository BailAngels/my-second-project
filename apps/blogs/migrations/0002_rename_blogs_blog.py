# Generated by Django 5.0 on 2023-12-07 08:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Blogs',
            new_name='Blog',
        ),
    ]
# Generated by Django 5.0.3 on 2024-03-07 12:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('art', '0003_remove_creation_published_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='exhibition',
            old_name='userid',
            new_name='author',
        ),
        migrations.RenameField(
            model_name='registerexhibition',
            old_name='userid',
            new_name='author',
        ),
        migrations.RenameField(
            model_name='teaching',
            old_name='userid',
            new_name='author',
        ),
    ]

# Generated by Django 5.0.3 on 2024-03-07 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('art', '0005_alter_teaching_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teaching',
            name='date',
            field=models.DateTimeField(verbose_name='%y/%m/%d'),
        ),
    ]

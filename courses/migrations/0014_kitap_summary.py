# Generated by Django 5.1.1 on 2024-12-25 06:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0013_slider'),
    ]

    operations = [
        migrations.AddField(
            model_name='kitap',
            name='summary',
            field=models.TextField(default=''),
        ),
    ]
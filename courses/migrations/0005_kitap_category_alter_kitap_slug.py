# Generated by Django 5.1.1 on 2024-11-07 08:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0004_alter_kitap_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='kitap',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='courses.category'),
        ),
        migrations.AlterField(
            model_name='kitap',
            name='slug',
            field=models.SlugField(blank=True, default='', unique=True),
        ),
    ]

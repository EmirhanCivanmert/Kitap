# Generated by Django 5.1.1 on 2024-11-08 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0008_remove_kitap_category_kitap_categories'),
    ]

    operations = [
        migrations.AddField(
            model_name='kitap',
            name='isHome',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='kitap',
            name='isActive',
            field=models.BooleanField(default=False),
        ),
    ]
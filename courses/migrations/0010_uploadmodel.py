# Generated by Django 5.1.1 on 2024-11-28 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0009_kitap_ishome_alter_kitap_isactive'),
    ]

    operations = [
        migrations.CreateModel(
            name='UploadModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images')),
            ],
        ),
    ]

# Generated by Django 4.2.5 on 2023-09-09 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_alter_gallery_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='gallery',
            name='branch',
            field=models.CharField(choices=[('Science', 'science'), ('Commerce', 'commerce'), ('Arts', 'arts')], default='science', max_length=100),
        ),
    ]

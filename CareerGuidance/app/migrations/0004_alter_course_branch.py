# Generated by Django 4.2.5 on 2023-09-08 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_rename_field_course_field_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='branch',
            field=models.CharField(choices=[('Science', 'science'), ('Commerce', 'commerce'), ('Arts', 'arts')], default='science', max_length=100),
        ),
    ]

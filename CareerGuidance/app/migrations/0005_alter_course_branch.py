# Generated by Django 4.2.5 on 2023-09-08 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_alter_course_branch'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='branch',
            field=models.CharField(choices=[('Science', 'science'), ('Commerce', 'commerce'), ('Arts', 'arts')], max_length=100),
        ),
    ]

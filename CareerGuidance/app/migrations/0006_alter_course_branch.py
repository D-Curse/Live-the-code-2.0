# Generated by Django 4.2.5 on 2023-09-08 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_alter_course_branch'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='branch',
            field=models.CharField(choices=[('Science', 'science'), ('Commerce', 'commerce'), ('Arts', 'arts')], default='commerce', max_length=100),
        ),
    ]

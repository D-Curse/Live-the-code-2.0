# Generated by Django 4.2.5 on 2023-09-08 10:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_course_branch'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='field',
            new_name='field_name',
        ),
    ]

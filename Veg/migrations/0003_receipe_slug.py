# Generated by Django 4.2 on 2023-05-05 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Veg', '0002_department_studentid_subject_student_subjectmarks'),
    ]

    operations = [
        migrations.AddField(
            model_name='receipe',
            name='slug',
            field=models.SlugField(blank=True, null=True, unique=True),
        ),
    ]

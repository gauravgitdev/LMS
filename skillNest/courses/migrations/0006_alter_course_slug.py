# Generated by Django 5.2.1 on 2025-05-27 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0005_alter_course_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='slug',
            field=models.CharField(blank=True, max_length=50, null=True, unique=True),
        ),
    ]

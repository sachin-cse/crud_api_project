# Generated by Django 4.1.5 on 2023-01-27 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_student_score'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='score',
        ),
        migrations.AddField(
            model_name='student',
            name='completed',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='student',
            name='description',
            field=models.TextField(default='No description provided.'),
        ),
    ]

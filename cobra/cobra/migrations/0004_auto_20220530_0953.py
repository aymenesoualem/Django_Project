# Generated by Django 3.1.14 on 2022-05-30 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cobra', '0003_course_remove_student_level'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='student',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]

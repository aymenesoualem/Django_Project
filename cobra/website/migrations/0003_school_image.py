# Generated by Django 4.0.4 on 2022-05-29 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_course'),
    ]

    operations = [
        migrations.AddField(
            model_name='school',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]

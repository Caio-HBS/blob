# Generated by Django 5.0.1 on 2024-01-09 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blob', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.SlugField(default='dasdasda', max_length=10, unique=True),
            preserve_default=False,
        ),
    ]

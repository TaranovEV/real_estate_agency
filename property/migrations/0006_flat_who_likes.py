# Generated by Django 2.2.24 on 2022-01-23 21:50

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('property', '0005_сomplaint'),
    ]

    operations = [
        migrations.AddField(
            model_name='flat',
            name='who_likes',
            field=models.ManyToManyField(related_name='flat_likes', to=settings.AUTH_USER_MODEL),
        ),
    ]

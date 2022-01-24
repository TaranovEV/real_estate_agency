# Generated by Django 2.2.24 on 2022-01-23 21:58

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0007_auto_20220124_0057'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flat',
            name='who_likes',
            field=models.ManyToManyField(blank=True, related_name='flat_likes', to=settings.AUTH_USER_MODEL, verbose_name='Кто лайкнул'),
        ),
    ]
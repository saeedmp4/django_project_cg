# Generated by Django 4.2 on 2023-05-02 13:03

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('testapp', '0005_blog_likes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='BlogLikes', to=settings.AUTH_USER_MODEL),
        ),
    ]
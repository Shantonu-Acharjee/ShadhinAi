# Generated by Django 4.2 on 2023-04-13 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("post", "0017_blog_new_slug"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="blog",
            name="new_slug",
        ),
        migrations.AddField(
            model_name="blog",
            name="custom_slug",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name="blog",
            name="slug",
            field=models.SlugField(blank=True, null=True, unique=True),
        ),
    ]

# Generated by Django 4.2 on 2023-04-09 08:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("post", "0005_blog_updated"),
    ]

    operations = [
        migrations.AddField(
            model_name="category",
            name="updated",
            field=models.DateTimeField(auto_now=True),
        ),
    ]

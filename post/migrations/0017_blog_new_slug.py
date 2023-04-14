# Generated by Django 4.2 on 2023-04-13 14:28

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("post", "0016_alter_blog_description"),
    ]

    operations = [
        migrations.AddField(
            model_name="blog",
            name="new_slug",
            field=autoslug.fields.AutoSlugField(
                blank=True,
                editable=False,
                null=True,
                populate_from="title",
                unique=True,
            ),
        ),
    ]
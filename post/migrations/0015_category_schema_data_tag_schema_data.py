# Generated by Django 4.2 on 2023-04-12 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("post", "0014_category_banner_category_high_regulation_banner_link_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="category",
            name="schema_data",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="tag",
            name="schema_data",
            field=models.TextField(blank=True, null=True),
        ),
    ]

# Generated by Django 4.2 on 2023-04-13 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("post", "0019_category_custom_slug_tag_custom_slug"),
    ]

    operations = [
        migrations.AlterField(
            model_name="tag",
            name="custom_slug",
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
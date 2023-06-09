# Generated by Django 4.2 on 2023-04-08 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("base", "0003_slider_image_link_alter_slider_banner"),
    ]

    operations = [
        migrations.CreateModel(
            name="HeaderLogo",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("brand_name", models.CharField(max_length=50)),
                (
                    "brang_logo",
                    models.ImageField(blank=True, null=True, upload_to="logo"),
                ),
                ("image_link", models.CharField(blank=True, max_length=300, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name="slider",
            name="slug",
        ),
        migrations.AlterField(
            model_name="slider",
            name="created_date",
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]

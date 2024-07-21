# Generated by Django 5.0.6 on 2024-07-21 02:04

import tinymce.models
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("posts", "0009_delete_course"),
    ]

    operations = [
        migrations.CreateModel(
            name="Course",
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
                ("title", models.CharField(max_length=75)),
                ("body", tinymce.models.HTMLField()),
                ("slug", models.SlugField()),
            ],
        ),
    ]

# Generated by Django 5.0.6 on 2024-07-21 01:57

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("posts", "0007_alter_post_title"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="slug",
            field=models.SlugField(blank=True, unique=True),
        ),
    ]

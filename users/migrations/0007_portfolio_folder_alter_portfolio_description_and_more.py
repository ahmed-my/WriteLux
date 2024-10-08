# Generated by Django 5.0.6 on 2024-08-09 03:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0006_folder"),
    ]

    operations = [
        migrations.AddField(
            model_name="portfolio",
            name="folder",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="portfolio_images",
                to="users.folder",
            ),
        ),
        migrations.AlterField(
            model_name="portfolio",
            name="description",
            field=models.TextField(blank=True, default="No decription provided"),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="portfolio",
            name="image",
            field=models.ImageField(upload_to="portfolio/"),
        ),
    ]

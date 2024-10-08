# Generated by Django 5.0.6 on 2024-05-26 09:25

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("fitness", "0004_fitness_banner_service_banner"),
    ]

    operations = [
        migrations.CreateModel(
            name="Image",
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
                ("image", models.ImageField(upload_to="images/")),
                (
                    "banner",
                    models.ImageField(blank=True, default="fallback.png", upload_to=""),
                ),
            ],
        ),
        migrations.DeleteModel(
            name="Service",
        ),
    ]

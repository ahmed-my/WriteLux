# Generated by Django 5.0.6 on 2024-07-21 00:56

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("posts", "0005_alter_course_body_alter_post_body"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="slug",
            field=models.SlugField(unique=True),
        ),
        migrations.AlterField(
            model_name="post",
            name="title",
            field=models.CharField(max_length=75, unique=True),
        ),
    ]

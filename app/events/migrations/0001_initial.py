# Generated by Django 4.2.1 on 2023-08-12 01:07

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Artist",
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
                ("first_name", models.CharField(max_length=50)),
                ("last_name", models.CharField(max_length=50)),
                (
                    "profile_picture",
                    models.ImageField(
                        blank=True,
                        default="cover_images/default_profile_picture.jpg",
                        upload_to="cover_images/",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Event",
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
                ("title", models.CharField(max_length=100)),
                ("description", models.TextField(blank=True, null=True)),
                (
                    "cover_image",
                    models.ImageField(blank=True, null=True, upload_to="cover_images/"),
                ),
                ("date", models.DateField(blank=True, default=datetime.date.today)),
                (
                    "image1",
                    models.ImageField(blank=True, null=True, upload_to="cover_images/"),
                ),
                (
                    "image2",
                    models.ImageField(blank=True, null=True, upload_to="cover_images/"),
                ),
                (
                    "image3",
                    models.ImageField(blank=True, null=True, upload_to="cover_images/"),
                ),
                (
                    "author",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="events.artist"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Article",
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
                ("title", models.CharField(max_length=100)),
                ("content", models.TextField(blank=True, null=True)),
                (
                    "cover_image",
                    models.ImageField(blank=True, null=True, upload_to="cover_images/"),
                ),
                (
                    "image1",
                    models.ImageField(blank=True, null=True, upload_to="cover_images/"),
                ),
                (
                    "image2",
                    models.ImageField(blank=True, null=True, upload_to="cover_images/"),
                ),
                (
                    "image3",
                    models.ImageField(blank=True, null=True, upload_to="cover_images/"),
                ),
                (
                    "author",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="events.artist"
                    ),
                ),
            ],
        ),
    ]

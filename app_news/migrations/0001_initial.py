# Generated by Django 5.0.6 on 2024-05-13 11:12

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="NewsModel",
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
                ("title_uz", models.CharField(max_length=255)),
                ("title_ru", models.CharField(max_length=255)),
                ("image", models.ImageField(blank=True, null=True, upload_to="")),
                ("date_time", models.DateTimeField(auto_now_add=True)),
                ("views", models.IntegerField(default=0)),
                ("content_uz", models.CharField(blank=True, max_length=500, null=True)),
                ("content_ru", models.CharField(blank=True, max_length=500, null=True)),
                ("description1_uz", models.TextField(blank=True, null=True)),
                ("description1_ru", models.TextField(blank=True, null=True)),
                ("description2_uz", models.TextField(blank=True, null=True)),
                ("description2_ru", models.TextField(blank=True, null=True)),
                ("description3_uz", models.TextField(blank=True, null=True)),
                ("description3_ru", models.TextField(blank=True, null=True)),
                ("advice1_uz", models.TextField(blank=True, null=True)),
                ("advice1_ru", models.TextField(blank=True, null=True)),
                ("advice2_uz", models.TextField(blank=True, null=True)),
                ("advice2_ru", models.TextField(blank=True, null=True)),
                ("advice3_uz", models.TextField(blank=True, null=True)),
                ("advice3_ru", models.TextField(blank=True, null=True)),
                (
                    "author",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name": "News",
                "verbose_name_plural": "News",
                "db_table": "news",
            },
        ),
    ]

# Generated by Django 5.0.1 on 2024-01-16 15:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("devtool", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Idea",
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
                ("title", models.CharField(max_length=24, verbose_name="아이디어명")),
                (
                    "image",
                    models.ImageField(
                        blank=True, upload_to="posts/%Y%m%d", verbose_name="이미지"
                    ),
                ),
                ("content", models.TextField(verbose_name="아이디어 설명")),
                ("interest", models.IntegerField(default=0, verbose_name="아이디어 관심도")),
                ("select", models.BooleanField(default=False)),
                (
                    "devtool",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="devtool.devtool",
                        verbose_name="예상 개발툴",
                    ),
                ),
            ],
        ),
    ]

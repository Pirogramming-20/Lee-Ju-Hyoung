# Generated by Django 5.0.1 on 2024-01-11 16:41

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("review", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="review",
            old_name="garde",
            new_name="grade",
        ),
    ]

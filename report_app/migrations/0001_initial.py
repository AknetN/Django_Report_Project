# Generated by Django 4.2.3 on 2023-07-11 12:05

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Report",
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
                ("title", models.CharField(max_length=255)),
                ("description", models.TextField()),
                (
                    "priority",
                    models.CharField(
                        choices=[
                            ("high", "High"),
                            ("urgent", "Urgent"),
                            ("soon", "Soon"),
                        ],
                        max_length=255,
                    ),
                ),
                ("completed", models.BooleanField(default=False)),
            ],
        ),
    ]
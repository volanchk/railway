# Generated by Django 4.2.6 on 2023-10-28 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Books",
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
                ("name", models.CharField(max_length=30)),
                ("topic", models.PositiveSmallIntegerField()),
                ("votes", models.PositiveIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name="Topics",
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
                ("topic", models.CharField(max_length=30, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name="Votes",
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
                ("topic", models.PositiveIntegerField()),
                ("user_id", models.PositiveIntegerField()),
                ("book_id", models.PositiveIntegerField()),
            ],
        ),
    ]

# Generated by Django 4.1.3 on 2022-11-03 01:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Movie",
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
                (
                    "title",
                    models.CharField(help_text="Título de la película", max_length=128),
                ),
                ("synopsis", models.TextField(help_text="Resumen de la película")),
            ],
        ),
        migrations.CreateModel(
            name="Director",
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
                (
                    "name",
                    models.CharField(help_text="Nombre del director", max_length=64),
                ),
                ("birth", models.DateField(help_text="Fecha de nacimiento")),
                ("dead", models.DateField(blank=True, help_text="Fecha de deceso")),
                ("phrase", models.TextField(help_text="Frases célebres")),
                (
                    "movies",
                    models.ManyToManyField(
                        blank=True, help_text="Películas dirigidas", to="miapp.movie"
                    ),
                ),
            ],
        ),
    ]

# Generated by Django 4.1.3 on 2022-11-03 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("miapp", "0003_phrase_alter_director_phrase"),
    ]

    operations = [
        migrations.AddField(
            model_name="phrase",
            name="name",
            field=models.CharField(
                default="vacío", help_text="Nombre del director", max_length=64
            ),
            preserve_default=False,
        ),
    ]

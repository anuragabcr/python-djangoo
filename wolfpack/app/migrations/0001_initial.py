# Generated by Django 4.1.4 on 2023-01-02 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Images",
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
                ("img1", models.ImageField(upload_to="images/")),
                ("img2", models.ImageField(upload_to="images/")),
                ("img3", models.ImageField(upload_to="images/")),
                ("img4", models.ImageField(upload_to="images/")),
            ],
        ),
    ]
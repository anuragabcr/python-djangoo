# Generated by Django 4.1.4 on 2023-01-06 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0005_review_reviewer"),
    ]

    operations = [
        migrations.AddField(
            model_name="review", name="avg_rating", field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name="review",
            name="num_rating",
            field=models.IntegerField(default=0),
        ),
    ]

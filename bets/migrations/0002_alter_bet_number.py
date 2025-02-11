# Generated by Django 4.2.18 on 2025-01-25 17:52

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("bets", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="bet",
            name="number",
            field=models.IntegerField(
                blank=True,
                null=True,
                validators=[
                    django.core.validators.MaxValueValidator(36),
                    django.core.validators.MinValueValidator(0),
                ],
            ),
        ),
    ]

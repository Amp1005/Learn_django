# Generated by Django 5.1.5 on 2025-02-22 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("vege", "0002_receipe_user"),
    ]

    operations = [
        migrations.AddField(
            model_name="receipe",
            name="receipe_view_count",
            field=models.IntegerField(default=1),
        ),
    ]

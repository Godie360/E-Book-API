# Generated by Django 5.0.4 on 2024-04-19 15:49

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("ebooks", "0003_alter_review_review"),
    ]

    operations = [
        migrations.AlterField(
            model_name="review",
            name="review",
            field=models.TextField(blank=True, null=True),
        ),
    ]

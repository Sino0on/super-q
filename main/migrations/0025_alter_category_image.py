# Generated by Django 5.1.7 on 2025-04-25 20:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0024_aboutimages_alter_sitesetting_director"),
    ]

    operations = [
        migrations.AlterField(
            model_name="category",
            name="image",
            field=models.FileField(upload_to="categories/", verbose_name="Изображение"),
        ),
    ]

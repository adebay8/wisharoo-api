# Generated by Django 4.2 on 2023-06-19 15:42

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("lists", "0002_alter_list_slug"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="list",
            name="address",
        ),
        migrations.AlterField(
            model_name="list",
            name="slug",
            field=models.CharField(default="GNrCLZv7UbpXQwB4daSFYZ", max_length=255),
        ),
        migrations.DeleteModel(
            name="ListAddress",
        ),
    ]

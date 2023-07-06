# Generated by Django 4.2 on 2023-06-20 22:43

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):
    dependencies = [
        ("lists", "0004_list_user_alter_list_slug"),
    ]

    operations = [
        migrations.AddField(
            model_name="list",
            name="event_date",
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="list",
            name="slug",
            field=models.CharField(default="SK9B6rYELJGvhypShaxXsv", max_length=255),
        ),
    ]

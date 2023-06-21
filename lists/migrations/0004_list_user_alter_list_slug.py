# Generated by Django 4.2 on 2023-06-20 22:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("lists", "0003_remove_list_address_alter_list_slug_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="list",
            name="user",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="user_lists",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AlterField(
            model_name="list",
            name="slug",
            field=models.CharField(default="BsAZ3APfoQSxrCv2BFa5e9", max_length=255),
        ),
    ]

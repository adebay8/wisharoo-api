# Generated by Django 4.2 on 2023-04-18 01:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("lists", "0004_listcollection_list_collection"),
    ]

    operations = [
        migrations.AlterField(
            model_name="list",
            name="collection",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="lists",
                to="lists.listcollection",
            ),
        ),
    ]
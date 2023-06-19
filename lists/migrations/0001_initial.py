# Generated by Django 4.2 on 2023-06-19 13:51

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='List',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('name', models.CharField(max_length=255)),
                ('cover_image', models.CharField(blank=True, max_length=255, null=True)),
                ('description', models.TextField(blank=True, max_length=255, null=True)),
                ('public', models.BooleanField(default=True)),
                ('slug', models.CharField(default='JLDr3xy3PX3VdKjanxYL8M', max_length=255)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ListAddress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('country', models.CharField(max_length=255)),
                ('line_one', models.CharField(max_length=255)),
                ('line_two', models.CharField(blank=True, max_length=255, null=True)),
                ('city', models.CharField(max_length=255)),
                ('state', models.CharField(max_length=255)),
                ('postcode', models.CharField(max_length=50)),
                ('public', models.BooleanField(default=True)),
                ('first_name', models.CharField(blank=True, max_length=255, null=True)),
                ('last_name', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ListCollection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, max_length=255, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ListItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('name', models.CharField(max_length=255)),
                ('note', models.TextField(blank=True, max_length=255, null=True)),
                ('link', models.CharField(blank=True, max_length=255, null=True)),
                ('price', models.FloatField(blank=True, null=True)),
                ('priority', models.IntegerField(choices=[(1, 'High priority'), (2, 'Medium priority'), (3, 'Low priority')], default=2)),
                ('quantity', models.IntegerField(blank=True, null=True)),
                ('unlimited_quantity', models.BooleanField(default=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ListItemCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, max_length=255, null=True)),
            ],
            options={
                'verbose_name_plural': 'List item categories',
            },
        ),
        migrations.CreateModel(
            name='ListItemImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('image', models.CharField(max_length=255)),
                ('list_item', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='images', to='lists.listitem')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='listitem',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='list_items', to='lists.listitemcategory'),
        ),
        migrations.AddField(
            model_name='listitem',
            name='list',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='list_items', to='lists.list'),
        ),
        migrations.CreateModel(
            name='ListImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('image', models.CharField(max_length=255)),
                ('list', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='images', to='lists.list')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='list',
            name='address',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='address_lists', to='lists.listaddress'),
        ),
        migrations.AddField(
            model_name='list',
            name='collection',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='collection_lists', to='lists.listcollection'),
        ),
    ]

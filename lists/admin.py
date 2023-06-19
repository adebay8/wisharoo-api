from django.contrib import admin
from . import models

# Register your models here.

admin.site.register(
    [
        models.List,
        models.ListItem,
        models.ListItemCategory,
        models.ListItemImage,
        models.ListCollection,
        models.ListImage,
    ]
)

from django.db import models
from wisharoo.mixins import ExtendedModelMixin
import uuid

# Create your models here.


class ListCollection(ExtendedModelMixin):
    name = models.CharField(max_length=255)
    description = models.TextField(max_length=255, null=True, blank=True)

    def __str__(self) -> str:
        return self.name


class ListAddress(ExtendedModelMixin):
    country = models.CharField(max_length=255)
    line_one = models.CharField(max_length=255)
    line_two = models.CharField(max_length=255, null=True, blank=True)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    postcode = models.CharField(max_length=50)
    public = models.BooleanField(default=True)
    first_name = models.CharField(max_length=255, null=True, blank=True)
    last_name = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.line_one}, {self.city}, {self.state}, {self.postcode}"


class List(ExtendedModelMixin):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)  # name has to be unique to the account
    cover_image = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(max_length=255, null=True, blank=True)
    public = models.BooleanField(default=True)
    custom_route = models.CharField(max_length=255, null=True, blank=True)
    collection = models.ForeignKey(
        ListCollection,
        null=True,
        on_delete=models.SET_NULL,
        related_name="collection_lists",
    )
    address = models.ForeignKey(
        ListAddress, null=True, on_delete=models.SET_NULL, related_name="address_lists"
    )

    def __str__(self) -> str:
        return self.name


class ListImage(ExtendedModelMixin):
    image = models.CharField(max_length=255)
    list = models.ForeignKey(
        List, on_delete=models.SET_NULL, related_name="images", null=True
    )


class ListItemCategory(ExtendedModelMixin):
    name = models.CharField(max_length=255)
    description = models.TextField(max_length=255, null=True, blank=True)

    class Meta:
        verbose_name_plural = "List item categories"

    def __str__(self) -> str:
        return self.name


class ListItem(ExtendedModelMixin):
    HIGH_PRIORITY = 1
    MEDIUM_PRIORITY = 2
    LOW_PRIORITY = 3

    PRIORITY_CHOICES = [
        (HIGH_PRIORITY, "High priority"),
        (MEDIUM_PRIORITY, "Medium priority"),
        (LOW_PRIORITY, "Low priority"),
    ]

    name = models.CharField(max_length=255)
    category = models.ForeignKey(
        ListItemCategory,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="list_items",
    )
    note = models.TextField(max_length=255, null=True, blank=True)
    link = models.CharField(max_length=255, null=True, blank=True)
    list = models.ForeignKey(
        List, on_delete=models.SET_NULL, related_name="list_items", null=True
    )
    price = models.FloatField(null=True, blank=True)
    priority = models.IntegerField(choices=PRIORITY_CHOICES, default=MEDIUM_PRIORITY)
    quantity = models.IntegerField(null=True, blank=True)
    unlimited_quantity = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.name


class ListItemImage(ExtendedModelMixin):
    image = models.CharField(max_length=255)
    list_item = models.ForeignKey(
        ListItem, on_delete=models.SET_NULL, related_name="images", null=True
    )

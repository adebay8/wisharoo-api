from . import models
from graphene_django import DjangoObjectType


class ListAddressType(DjangoObjectType):
    class Meta:
        model = models.ListAddress
        fields = "__all__"


class ListImageType(DjangoObjectType):
    class Meta:
        model = models.ListImage
        fields = "__all__"


class ListCollectionType(DjangoObjectType):
    class Meta:
        model = models.ListCollection
        fields = "__all__"


class ListType(DjangoObjectType):
    class Meta:
        model = models.List
        fields = "__all__"

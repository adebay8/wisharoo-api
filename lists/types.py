from . import models
from graphene_django import DjangoObjectType
import graphene


class CreateListInputType(graphene.InputObjectType):
    name = graphene.String(required=True)
    description = graphene.String()
    cover_image = graphene.String()
    public = graphene.Boolean()
    custom_route = graphene.String()
    address = graphene.Int()
    collection = graphene.Int()


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

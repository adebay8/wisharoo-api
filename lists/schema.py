import graphene
from graphene_django import DjangoObjectType
from . import models, types


class Query(graphene.ObjectType):
    lists = graphene.List(types.ListType)

    def resolve_lists(root, info, **kwargs):
        return models.List.objects.select_related("collection", "address").all()


schema = graphene.Schema(query=Query)

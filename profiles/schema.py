import graphene
from . import types
from django.contrib.auth import get_user_model


class Query(graphene.ObjectType):
    all_users = graphene.List(types.UserType)

    def resolve_all_users(root, info):
        return get_user_model().objects.all()


class Mutation(graphene.ObjectType):
    pass


schema = graphene.Schema(mutation=Mutation, query=Query)

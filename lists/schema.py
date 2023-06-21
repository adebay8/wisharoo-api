import graphene
from graphene_django import DjangoObjectType
from . import models, types
from datetime import datetime
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model


class Query(graphene.ObjectType):
    lists = graphene.List(
        types.ListType, uuid=graphene.String(), slug=graphene.String()
    )
    list = graphene.Field(
        types.ListType, uuid=graphene.String(required=True), slug=graphene.String()
    )

    def resolve_lists(root, info, **kwargs):
        # filter_kwargs = {}

        # if "uuid" in kwargs:
        #     filter_kwargs["uuid"] = kwargs.get("uuid")
        # if "slug" in kwargs:
        #     filter_kwargs["slug"] = kwargs.get("slug")

        if len(kwargs) > 0:
            try:
                return models.List.objects.select_related("collection", "user").filter(
                    **kwargs
                )
            except models.List.DoesNotExist:
                return None

        return models.List.objects.select_related("collection", "user").all()

    def resolve_list(root, info, **kwargs):
        try:
            models.List.objects.select_related("collection", "address").get(
                uuid=kwargs.get("uuid")
            )
        except models.List.DoesNotExist:
            return None


class CreateList(graphene.Mutation):
    class Arguments:
        list = types.CreateListInputType(required=True)

    success = graphene.Boolean()
    list = graphene.Field(types.ListType)
    message = graphene.String()

    def mutate(root, info, **kwargs):
        if "list" not in kwargs:
            return None

        try:
            data = kwargs.get("list")

            list = models.List(
                name=data.name,
                description=data.description,
                cover_image=data.cover_image,
                event_date=datetime.strptime(data.event_date, "%Y-%m-%d"),
                user=get_user_model().objects.get(uuid=data.user),
            )

            if "public" in data:
                list.public = data.public
            if "slug" in data:
                list.slug = data.slug

            list.full_clean()
            list.save()

            return CreateList(list=list, success=True)
        except Exception as e:
            return CreateList(list=None, success=False, message=str(e))


class UpdateList(graphene.Mutation):
    class Arguments:
        uuid = graphene.UUID(required=True)

    success = graphene.Boolean()

    def mutate(root, info, **kwargs):
        return UpdateList(success=True)


class DeleteList(graphene.Mutation):
    class Arguments:
        uuid = graphene.UUID(required=True)

    success = graphene.Boolean()

    def mutate(root, info, **kwargs):
        return DeleteList(success=True)


class Mutation(graphene.ObjectType):
    createList = CreateList.Field()
    updateList = UpdateList.Field()
    deleteList = DeleteList.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)

import graphene
from graphene_django import DjangoObjectType
from . import models, types


class Query(graphene.ObjectType):
    lists = graphene.List(types.ListType, uuid=graphene.String())
    list = graphene.Field(types.ListType, uuid=graphene.String(required=True))

    def resolve_lists(root, info, **kwargs):
        if "uuid" in kwargs:
            try:
                return models.List.objects.select_related().filter(
                    uuid=kwargs.get("uuid")
                )
            except models.List.DoesNotExist:
                return None
        return models.List.objects.select_related("collection", "address").all()

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

    def mutate(root, info, **kwargs):
        if "list" not in kwargs:
            return None

        try:
            data = kwargs.get("list")

            list = models.List(
                name=data.name,
                description=data.description,
                cover_image=data.cover_image,
                public=data.public,
                custom_route=data.custom_route,
            )

            if "address" in data:
                try:
                    address = models.ListAddress.objects.get(pk=address)
                    list.address = address
                except:
                    list.address = None

            if "collection" in data:
                try:
                    collection = models.ListCollection.objects.get(pk=address)
                    list.collection = collection
                except:
                    list.collection = None

            list.save()

            return CreateList(list=list, success=True)
        except:
            return CreateList(list=None, success=False)


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

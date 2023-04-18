import graphene
from lists.schema import schema as ListSchema


class Query(ListSchema.query, graphene.ObjectType):
    hello = graphene.String(default_value="Hi!")


schema = graphene.Schema(query=Query)

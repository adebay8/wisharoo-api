import graphene
from lists.schema import schema as ListSchema
from timelines.schema import schema as TimelineSchema


class Query(ListSchema.query, TimelineSchema.query, graphene.ObjectType):
    pass


class Mutation(ListSchema.mutation, TimelineSchema.mutation, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)

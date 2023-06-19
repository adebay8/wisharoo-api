import graphene
import graphql_jwt
from lists.schema import schema as ListSchema
from timelines.schema import schema as TimelineSchema
from profiles.schema import schema as ProfileSchema


class Query(
    ListSchema.query, TimelineSchema.query, ProfileSchema.query, graphene.ObjectType
):
    pass


class Mutation(
    ListSchema.mutation,
    TimelineSchema.mutation,
    ProfileSchema.mutation,
    graphene.ObjectType,
):
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()
    revoke_token = graphql_jwt.Revoke.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)

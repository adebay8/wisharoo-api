import graphene


class TimelineItemType(graphene.ObjectType):
    id = graphene.String(required=True)
    description = graphene.String(required=True)
    image_url = graphene.String(required=True)
    url = graphene.String(required=True)

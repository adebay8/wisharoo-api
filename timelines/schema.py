import graphene
import requests
from . import types


class Query(graphene.ObjectType):
    getTimeline = graphene.List(
        types.TimelineItemType,
        keyword=graphene.String(required=True),
        per_page=graphene.Int(),
        page=graphene.Int(),
    )

    def resolve_getTimeline(root, info, keyword, **kwargs):
        params = {
            "query": keyword,
        }

        params["per_page"] = kwargs.get("per_page") if "per_page" in kwargs else 20
        params["page"] = kwargs.get("page") if "page" in kwargs else 1

        response = requests.get(
            "https://api.unsplash.com/search/photos",
            headers={
                "Accept-Version": "v1",
                "Authorization": "Client-ID Npjw5uYueynLuPOHgNTpZpmEMzi4sWUKsCqqrtzIRuw",
            },
            params=params,
        )

        results = response.json()["results"]
        timeline = [
            {
                "id": result["id"],
                "description": result["alt_description"],
                "image_url": result["urls"]["small"],
                "url": result["links"]["html"],
            }
            for result in results
        ]

        return timeline


class Mutation(graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)

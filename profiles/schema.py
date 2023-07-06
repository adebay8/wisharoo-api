import graphene
from . import types, models, helpers
from django.contrib.auth import get_user_model
from graphql_jwt.decorators import staff_member_required
from django.db import IntegrityError


class Query(graphene.ObjectType):
    all_users = graphene.List(types.UserType)
    user = graphene.Field(types.UserType, uuid=graphene.String(required=True))

    @staff_member_required
    def resolve_all_users(root, info):
        return get_user_model().objects.all()

    def resolve_user(root, info, **kwargs):
        return get_user_model().objects.get(uuid=kwargs.get("uuid"))


class CreateUser(types.APIResponseType, graphene.Mutation):
    class Arguments:
        user = types.CreateUserInputType(required=True)

    user = graphene.Field(types.UserType)

    def mutate(root, info, user):
        try:
            new_user, created = get_user_model().objects.get_or_create(
                email=user.email, username=user.username
            )

            if not created:
                raise Exception(
                    "Username ({}) and email ({}) are already taken".format(
                        user.username, user.email
                    )
                )

            new_user.set_password(user.password)
            new_user.save()

            return CreateUser(user=new_user, success=True)
        except IntegrityError as e:
            return CreateUser(
                success=False,
                error={"type": type(e).__name__, "code": 409, "message": str(e)},
            )
        except Exception as e:
            return CreateUser(
                success=False,
                error={"type": type(e).__name__, "code": 408, "message": str(e)},
            )


class CreateWaitlistUser(types.APIResponseType, graphene.Mutation):
    class Arguments:
        first_name = graphene.String(required=True)
        last_name = graphene.String(required=True)
        email = graphene.String(required=True)

    user = graphene.Field(types.WaitlistUserType)

    def mutate(root, info, **kwargs):
        try:
            waitlist_user, created = models.WaitlistUser.objects.get_or_create(**kwargs)
            waitlist_user.save()

            template = helpers.TemplateEmail(
                to=kwargs.get("email"),
                subject=f"Welcome to Wisharoo! Join our Waitlist and Discover a World of Wishes",
                template="waitlist",
                context={"firstName": kwargs.get("first_name")},
            )
            template.send()

            return CreateWaitlistUser(user=waitlist_user, success=True)
        except Exception as e:
            return CreateWaitlistUser(success=False)


class SendEmail(types.APIResponseType, graphene.Mutation):
    class Arguments:
        type = graphene.String(required=True)
        recipient_email = graphene.String(required=True)
        recipient_first_name = graphene.String(required=True)

    def mutate(root, info, **kwargs):
        try:
            template = helpers.TemplateEmail(
                to=kwargs.get("recipient_email"),
                subject=f"Welcome to Wisharoo! Join our Waitlist and Discover a World of Wishes",
                template="waitlist",
                context={"firstName": kwargs.get("recipient_first_name")},
            )
            template.send()

            return SendEmail(success=True)
        except Exception as e:
            return SendEmail(
                success=False,
                error={"type": type(e).__name__, "code": 400, "message": str(e)},
            )


class Mutation(graphene.ObjectType):
    create_user = CreateUser.Field()
    create_waitlist_user = CreateWaitlistUser.Field()
    send_waitlist_email = SendEmail.Field()


schema = graphene.Schema(mutation=Mutation, query=Query)

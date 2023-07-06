from graphene_django import DjangoObjectType
from django.contrib.auth import get_user_model
from . import models
from graphene import InputObjectType, ObjectType
import graphene


class UserType(DjangoObjectType):
    class Meta:
        model = get_user_model()
        fields = "__all__"


class UserProfileType(DjangoObjectType):
    class Meta:
        model = models.UserProfile
        fields = "__all__"


class UserAddressType(DjangoObjectType):
    class Meta:
        model = models.UserAddress
        fields = "__all__"


class CreateUserInputType(InputObjectType):
    email = graphene.String(required=True)
    username = graphene.String(required=True)
    password = graphene.String(required=True)


class APIErrorType(ObjectType):
    type = graphene.String()
    message = graphene.String()
    code = graphene.Int()


class APIResponseType:
    success = graphene.Boolean()
    error = graphene.Field(APIErrorType)


class WaitlistUserType(DjangoObjectType):
    class Meta:
        model = models.WaitlistUser
        fields = "__all__"

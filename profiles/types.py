from graphene_django import DjangoObjectType
from django.contrib.auth import get_user_model
from . import models


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

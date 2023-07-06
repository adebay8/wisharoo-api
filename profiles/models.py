from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from wisharoo.mixins import ExtendedModelMixin


# Create your models here.


class User(AbstractUser, ExtendedModelMixin):
    email = models.EmailField(_("email address"), unique=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username", "first_name", "last_name"]

    def __str__(self):
        return "{}".format(self.email)


class UserProfile(ExtendedModelMixin):
    user = models.OneToOneField(
        get_user_model(), on_delete=models.SET_NULL, null=True, related_name="profile"
    )
    phone_number = models.CharField(max_length=50, blank=True)
    website = models.CharField(max_length=255, blank=True)
    photo = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.user.get_username()


class UserAddress(ExtendedModelMixin):
    country = models.CharField(max_length=255)
    line_one = models.CharField(max_length=255)
    line_two = models.CharField(max_length=255, null=True, blank=True)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    postcode = models.CharField(max_length=50)
    public = models.BooleanField(default=True)
    user = models.ForeignKey(
        get_user_model(), on_delete=models.SET_NULL, null=True, related_name="addresses"
    )

    def __str__(self) -> str:
        return f"{self.line_one}, {self.city}, {self.state}, {self.postcode}"


class WaitlistUser(ExtendedModelMixin):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField()

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)

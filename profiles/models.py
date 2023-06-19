from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from wisharoo.mixins import ExtendedModelMixin


# Create your models here.
class User(AbstractUser):
    email = models.EmailField(_("email address"), unique=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username", "first_name", "last_name"]

    def __str__(self):
        return "{}".format(self.email)


class UserProfile(ExtendedModelMixin):
    user = models.OneToOneField(get_user_model(), on_delete=models.SET_NULL, null=True)
    phone_number = models.CharField(max_length=50, blank=True)
    website = models.CharField(max_length=255, blank=True)
    photo = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.user.get_username()

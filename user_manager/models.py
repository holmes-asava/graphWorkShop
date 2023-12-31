import uuid

from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models

from user_manager.managers import UserManager
from django.apps import apps


class User(AbstractBaseUser, PermissionsMixin):
    id = models.UUIDField("ID", primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(
        "email address", unique=True, default=None, blank=True, null=True
    )
    first_name = models.CharField("first name", max_length=32, blank=True)
    last_name = models.CharField("last name", max_length=32, blank=True)
    is_staff = models.BooleanField("staff status", default=False)
    USERNAME_FIELD = "email"
    objects = UserManager()


class Node(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)


class Author(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    node = models.ForeignKey(Node, on_delete=models.CASCADE)

from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models


class CustomUser(AbstractUser):
    """ 

    A custom user model that extends Django's default User model. 

    Attributes:
        is_premium (bool): Indicates whether the user has a premium subscription.
        groups (ManyToManyField): Related groups for the user.
            This overrides the default related_name to avoid reverse accessor clashes.
        user_permissions (ManyToManyField): Related permissions for the user.
            This overrides the default related_name to avoid reverse accessor clashes.
    """

    is_premium = models.BooleanField(
        default=False,
        help_text="Indicates if the user has a premium subscription."
    )

    groups = models.ManyToManyField(
        Group,
        related_name="customuser_set",
        blank=True,
        help_text="Groups the user belongs to."
    )

    user_permissions = models.ManyToManyField(
        Permission,
        related_name="customuser_set",
        blank=True,
        help_text="Specific permissions assigned to the user."
    )

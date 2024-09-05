from django.contrib.auth.models import AbstractUser
from django.db import models

# Define user types
USER_TYPE_CHOICES = (
    ('farmer', 'Farmer'),
    ('buyer', 'Buyer'),
    ('expert', 'Expert'),
)

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    user_type = models.IntegerField(choices=USER_TYPE_CHOICES)

    # Add related_name to avoid conflict with auth.User groups and user_permissions
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='customuser_set',  # Change related_name to avoid conflict
        blank=True
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='customuser_set',  # Change related_name to avoid conflict
        blank=True
    )

    def __str__(self):
        return self.username

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        verbose_name = 'Custom User'
        verbose_name_plural = 'Custom Users'

        permissions = [
            ("can_view_custom_content", "Can view custom content"),
            ("can_edit_custom_content", "Can edit custom content"),
        ]
        ordering = ['user_type']

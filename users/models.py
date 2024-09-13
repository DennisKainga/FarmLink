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
    user_type = models.CharField(
        max_length=10, choices=USER_TYPE_CHOICES)

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='customuser_set',
        blank=True
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='customuser_set',
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

    class Meta:
        verbose_name = 'Custom User'
        verbose_name_plural = 'Custom Users'

        permissions = [
            ("can_view_custom_content", "Can view custom content"),
            ("can_edit_custom_content", "Can edit custom content"),
        ]
        ordering = ['user_type']

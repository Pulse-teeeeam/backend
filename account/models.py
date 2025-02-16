from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    phone = models.CharField(max_length=11, null=True, blank=True)
    code_etc = models.IntegerField(unique=True, null=True, blank=True)

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='customuser_set',
        blank=True,
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='customuser_permissions_set',
        blank=True,
    )

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'Юзер'
        verbose_name_plural = 'Юзеры'
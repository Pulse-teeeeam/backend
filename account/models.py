from django.db import models
from django.contrib.auth.models import AbstractUser

# class CustomUser(AbstractUser):
#     phone = models.CharField(max_length=11, unique=True)
#
#     class Meta:
#         verbose_name = 'Юзер'
#         verbose_name_plural = 'Юзеры'
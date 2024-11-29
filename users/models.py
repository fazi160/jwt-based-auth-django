from django.contrib.auth.models import AbstractUser
from django.db import models



class User(AbstractUser):
    USER_TYPE_CHOICES = [
        ('user', 'User'),
        ('author', 'author'),
        ('admin', 'admin'),
    ]

    user_type = models.CharField(
        max_length=50,
        choices=USER_TYPE_CHOICES,
        default='user',
    )
    is_permitted = models.BooleanField(default=False)
    


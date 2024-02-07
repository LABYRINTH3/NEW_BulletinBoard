from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class CustomUser(AbstractUser):
    username = models.CharField(
        max_length=150,
        unique=True,
        help_text=""
    )
    pass

    def __str__(self):
        return self.username

from django.db import models
from django.contrib.auth.models import AbstractUser

class BookExample(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class User(AbstractUser):
    # Librarians are pro users
    is_pro = models.BooleanField(default=False)

    def __str__(self):
        return self.username

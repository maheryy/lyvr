from django.db import models

class BookExample(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.title

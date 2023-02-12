from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
from datetime import datetime,timedelta


class User(AbstractUser):
    # Librarians are pro users
    username = models.CharField(max_length=100)
    email = models.EmailField(primary_key=True)
    password = models.CharField(max_length=100)
    is_pro = models.BooleanField(default=False)

    def __str__(self):
        return self.username

class Book(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    editor = models.CharField(max_length=100)
    collection = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    cover = models.ImageField(upload_to='covers', blank=True, null=True)

    def __str__(self):
        return self.title

class Library(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Loan(models.Model):
    id = models.AutoField(primary_key=True)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    library = models.ForeignKey(Library, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    loan_date = models.DateField()
    return_date = models.DateField()
    is_returned = models.BooleanField(default=False)

    def __str__(self):
        return self.book

class Message(models.Model):
    id = models.AutoField(primary_key=True)
    user1 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user1')
    user2 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user2')
    message = models.CharField(max_length=1000)
    date = models.DateField()

    def __str__(self):
        return self.message

class ReadingGroup(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    library = models.ForeignKey(Library, on_delete=models.CASCADE)



    def __str__(self):
        return self.name

class Forum(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    reading_group = models.ForeignKey(ReadingGroup, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Comment(models.Model):
    id = models.AutoField(primary_key=True)
    content = models.CharField(max_length=1000)
    date = models.DateField()
    forum = models.ForeignKey(Forum, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.content
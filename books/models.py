from django.db import models
from django.contrib.auth.models import User


class Book(models.Model):
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    subject = models.CharField(max_length=50)
    year = models.CharField(max_length=4)
    count = models.IntegerField(max_length=4)
    description = models.TextField()
    isbn = models.CharField(max_length=10)


class LendBook(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)

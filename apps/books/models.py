from __future__ import unicode_literals

from django.db import models
# from apps.login.models import User

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="books")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Book_review(models.Model):
    # One user can review many books
    user = models.ForeignKey('login.User', on_delete=models.CASCADE, related_name="reviewed_books")
    # One book can be reviewed by many users
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="reviewed_by_users")
    review = models.TextField()
    rating = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
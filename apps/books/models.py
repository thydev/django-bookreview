from __future__ import unicode_literals
from django.db import models

class AuthorManager(models.Manager):
    def create_validator(self, postData):
        errors = {}
        if len(postData['author_new']) < 2:
            errors["author"] = "Author name should be more than 2 characters"
        elif Author.objects.filter(name=postData['author_new']).count() > 0:
            errors['author'] = "This author name {} already exists".format(postData['author_new'])

        return errors

class BookManager(models.Manager):
    def create_validator(self, postData):
        errors = {}
        if len(postData['title']) < 2:
            errors["title"] = "Title should be more than 2 characters"
        elif Book.objects.filter(title=postData['title']).count() > 0:
            errors['title'] = "This book title {} already exists".format(postData['title'])

        return errors

class Book_ReviewManager(models.Manager):
    def create_validator(self, postData):
        errors = {}
        if len(postData['review']) < 5:
            errors["title"] = "Title should be more than 5 characters"
        return errors


class Author(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = AuthorManager()

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="books")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = BookManager()
    reviewers = models.ManyToManyField('login.User', through='Book_Review', related_name="reviewed_books")

# Many to many relationship between users and books
class Book_Review(models.Model):
    # One user can review many books
    user = models.ForeignKey('login.User', on_delete=models.CASCADE, related_name="user_reviews")
    # One book can be reviewed by many users
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="book_reviews")

    review = models.TextField()
    rating = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = Book_ReviewManager()
from django.db import models
from datetime import datetime
from login.models import User

# Create your models here.
# class User(models.Model):
#     first_name = models.CharField(max_length=50)
#     last_name = models.CharField(max_length=50)
#     email = models.CharField(max_length=50)
#     password = models.CharField(max_length=70)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

##    books_uploaded
##    books_liked

class BookManager(models.Manager):
    def basic_validator(self, postData):
        errors={}
        if postData['title'] == '':
            errors['title'] = 'Title is required'
        elif Book.objects.filter(title__iexact=postData['title']):
            errors['title'] = 'This book already exists'
        if len(postData['desc']) < 5:
            errors['desc'] = 'Description should be at least 5 characters in length'
        return errors

    def edit_validator(self, postData,bookid):
        errors={}
        if postData['title'] == '':
            errors['title'] = 'Title is required'
        elif Book.objects.filter(title__iexact=postData['title']).exclude(id=bookid):
            errors['title'] = 'This book already exists'
        if len(postData['desc']) < 5:
            errors['desc'] = 'Description should be at least 5 characters in length'
        return errors

class Book(models.Model):
    title = models.CharField(max_length=255)
    desc = models.TextField()
    uploaded_by = models.ForeignKey(User, related_name="books_uploaded", on_delete=models.CASCADE)
    liked_by = models.ManyToManyField(User, related_name="books_liked")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = BookManager()
        
    def __repr__(self):
        return f"{self.id} - {self.title}"

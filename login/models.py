from django.db import models
import re
from datetime import datetime
import bcrypt

class UserManager(models.Manager):
    def basic_validator(self, postData):
        errors={}
        if len(postData['first_name']) < 2:
            errors['first_name'] = "First name must be at least 2 characters in length"

        if len(postData['last_name']) < 2:
            errors['last_name'] = "Last name must be at least 2 characters in length"
        
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['email']):
            errors['email'] = "Please enter a valid email address"
        elif len(User.objects.filter(email__iexact=postData['email'])) > 0:
            errors['email'] = "An account already exists for this email"

        PW_REGEX = re.compile(r'^(?=.*\d)[a-zA-Z\d]{8,20}$')
        if not PW_REGEX.match(postData['password']):
            errors['password'] = "Password must be between 8-20 characters in length and must contain at least one number"
        
        if not postData['password'] == postData['confirmpw']:
            errors['confirmpw'] = "Passwords do not match. Please confirm password again"

        
        if postData['birth_date'] == '':
            errors['birth_date'] = "Please enter date of birth"
        else:
            birthday = datetime.strptime(postData['birth_date'], '%Y-%m-%d').date()
            today = datetime.utcnow().date()
            if birthday > today:
                errors['birth_date'] = "Date of birth must be in the past"
            elif (birthday.year + 13, birthday.month, birthday.day) > (today.year, today.month, today.day):
                errors['birth_date'] = "You must be at least 13 years old to register"

        return errors      

    def pw_validator(self, postData):
        errors={}
        user = User.objects.filter(email=postData['logemail'])
        if user:
            logged_user = user[0]
            if bcrypt.checkpw(postData['logpassword'].encode(), logged_user.password.encode()) == False:
                errors = {'login_failed': 'Incorrect email or password'}
        else:
            errors = {'login_failed': 'Incorrect email or password'}

        return errors


# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=70)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

    def __repr__(self):
        return f"{self.first_name} {self.last_name} ({self.email})"
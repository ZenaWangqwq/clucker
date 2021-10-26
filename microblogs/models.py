from django.db import models
from django.db.models import Model
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.conf import settings
from datetime import date

# Create your models here.

class User(AbstractUser):
    username = models.CharField(
        max_length = 30,
        unique = True,
        validators = [RegexValidator(
            regex = r'^@\w{3,}$',
            message = 'Username must consist of @ followed by at least 3 alphanumericals'
        )]
    )

    first_name = models.CharField(blank = False,max_length = 50,unique = False)
    last_name = models.CharField(blank = False,max_length = 50,unique = False)
    email = models.EmailField(unique = True,blank = False)
    bio = models.CharField(max_length = 520, blank = True)

class Post(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        blank=False
    )
    text = models.CharField(max_length = 280)
    created_at = models.DateTimeField(default=date.today)

    class Meta:
        ordering = ['created_at']

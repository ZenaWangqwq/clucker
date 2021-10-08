from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator

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

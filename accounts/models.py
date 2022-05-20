from django.db import models
from .manager import AccountManager
from django.contrib.auth.models import AbstractBaseUser
# Create your models here.

class Account(AbstractBaseUser):
    email = models.EmailField(verbose_name= "Email", max_length= 50, null=False, unique = True)
    username = models.CharField(max_length= 50, unique= True)
    date_joined = models.DateTimeField(verbose_name= "Date Joined", auto_now_add=True)
    last_login = models.DateTimeField(verbose_name= "Last Login", auto_now=True)
    is_admin = models.BooleanField(default = False)
    is_staff = models.BooleanField(default= False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default= False)
    hide_email = models.BooleanField(default= True)

    objects = AccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS= ['username']

    def __str__(self):
        return self.username

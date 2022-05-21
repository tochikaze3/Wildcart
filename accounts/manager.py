from django.db import models
from django.contrib.auth.models import BaseUserManager



class AccountManager(BaseUserManager):
    
    def create_user(self, email, password=None):
       if not email:
           raise ValueError("Users must have an email address")
       user = self.model(
               email= self.normalize_email(email),
        )
       user.set_password(password)
       user.save(using=self._db)
       return user

    def create_superuser(self, email, password):
        user = self.create_user(
            email= self.normalize_email(email),
            password=password,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user
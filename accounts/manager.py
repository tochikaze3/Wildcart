from django.db import models
from django.contrib.auth.models import BaseUserManager



class AccountManager(BaseUserManager):
    
    def _create_user(self, email, password, mobile, **extra_fields):
       if not email:
           raise ValueError("Users must have an email address")
       if not password: 
           raise ValueError("Users must have a password")
       user = self.model(
               email= self.normalize_email(email),
               mobile = mobile,
               **extra_fields
        )
       user.set_password(password)
       user.save(using=self._db)
       return user



    def create_user(self, email, password, mobile, **extra_fields):
       extra_fields.setdefault('is_staff', True)
       extra_fields.setdefault('is_active', True)
       extra_fields.setdefault('is_superuser', False)
       return self._create_user(email, password, mobile, **extra_fields)

    def create_superuser(self, email, password, mobile, **extra_fields):
       extra_fields.setdefault('is_staff', True)
       extra_fields.setdefault('is_active', True)
       extra_fields.setdefault('is_superuser', True)
       return self._create_user(email, password, mobile, **extra_fields) 
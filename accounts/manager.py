from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import ugettext_lazy as _


class UserManager(BaseUserManager):

 def create_user(self, email, password, **extra_fields):
    
        if not email:
            raise ValueError(_('You have to set an email'))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()

def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff = True. '))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser = True.'))
        return self.create_user(email, password, **extra_fields)




'''
class UserManager(BaseUserManager):

    def create_user(self, username, email, password = None):

        if username is None:
            raise TypeError('Users should have a username')
        if not email:
            raise TypeError(_('You have to set an email'))
        email = self.normalize_email(email)
        user = self.model(username=username, email=email)
        user.set_password(password)
        user.save()p

        

    def create_superuser(self, username, email, password=None):
        
        if password is None:
                raise TypeError('password must be filled')

        user = self.create_user(username, email, password)
        #user.is_superuser = True
        #user.is_staff = False
        user.save()
        return user'''
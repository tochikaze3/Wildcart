from django.contrib.auth.base_user import AbstractBaseUser,BaseUserManager
from django.utils.translation import ugettext_lazy as _

class UserManager(BaseUserManager):

    def create_user(self, username, email, password = None):

        if username is None:
            raise TypeError('Users should have a username')
        if not email:
            raise TypeError(_('You have to set an email'))
        email = self.normalize_email(email)
        user = self.model(username=username, email=email)
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, username, email, password=None):
        
        if password is None:
                raise TypeError('password must be filled')

        user = self.create_user(username, email, password)
        user.is_superuser = True
        user.is_staff = True
        user.save()
        return user
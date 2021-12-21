from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

class UserManager(BaseUserManager):
# The create_user method is passed
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('User must have an email address')

# Create a user from the UserModel
# Use the normalize_email method from the BaseUserManager to
# normalize the domain of the email

        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save()
        return user

# Create the user with the custom create_user method above and add the is_superuser and is_staff properties

    def create_superuser(self, email, password):
        user = self.create_user(email, password)
        user.is_superuser = True
        user.is_staff = True
        user.save()
        return user


# Inherit from AbstractBaseUser and PermissionsMixin
class User(AbstractBaseUser, PermissionsMixin):
# Django model with required fields type and option
    email = models.EmailField(max_length=255, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

# Override Django default username to use email instead
    USERNAME_FIELD = 'email'

    def __str__(self):
        """Return string representation of the user"""
        return self.email

    objects = UserManager()

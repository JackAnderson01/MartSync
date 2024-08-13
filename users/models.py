import uuid
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _
from django.conf import settings

class UserManager(BaseUserManager):

    # Normal user creation
    def create_user(self, email, password, **extra_fields):

        if not email:
            # raise an  value error if this function is being called without an email.
            raise ValueError(_("Email is required."))

        
        email = self.normalize_email(email)

        # Adding a new user with the provided email to the model
        user = self.model(email=email, **extra_fields)

        # Setting the password of the user using set_password method to encrypt the password
        user.set_password(password)

        # Saving the user details into the database.
        user.save()

        # Returning the user.
        return user
    
    # Super user creation
    def create_superuser(self, email, password, **extra_fields):

        # Setting extra fields to True
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_("Superuser must be assigned with is_staff set to True."))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_("Superuser must be assigned with is_superuser set to True."))

        return self.create_user(email, password, **extra_fields)
    

class User(AbstractBaseUser, PermissionsMixin):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(_('email address'), unique=True)
    name = models.CharField(_('name'), max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    otp = models.CharField(max_length=6)
    otp_expiry = models.DateTimeField(blank=True, null=True)
    max_otp_try = models.CharField(max_length=2, default=settings.MAX_OTP_TRY)
    otp_max_out = models.DateTimeField(blank=True, null=True)
    is_verified = models.BooleanField(null=True, blank=True)
    is_active = models.BooleanField(null=False, blank=False, default=False)
    is_staff = models.BooleanField(null=False, blank=False, default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']


    objects = UserManager()


    def __str__(self):
        return self.email
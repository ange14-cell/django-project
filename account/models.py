from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager

class MyUserManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError("vous devez entrez un email")
        user = self.model(
            email=self.normalize_email(email)
        )
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password=None):
        user = self.create_user(email=email, password=password)
        user.is_admin = True
        user.is_staff = True
        user.save()
        return user

class Shopper(AbstractBaseUser):
    email = models.EmailField(
        unique=True,
        max_length=250,
        blank=True,
    )
    username = models.CharField(max_length=250)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    objects = MyUserManager()

    def has_perm(self, perm, obj=None):
       return True

    def has_module_perms(self, app_label):
       return True
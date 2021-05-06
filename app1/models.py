from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db.models.fields.related import ForeignKey
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from .manager import CustomUserManager
# Create your models here.
class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'), unique=True)
    name = models.CharField(max_length=500,default="",null=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    objects = CustomUserManager()

    def __str__(self):
        return self.email


class Advisor(models.Model):
    advisor_name=models.CharField(max_length=500,null=False)
    advisor_photo_url=models.CharField(max_length=1000,null=False)

    def __str__(self):
        return self.advisor_name



class Bookings(models.Model):
    advisor=models.ForeignKey(Advisor,on_delete=models.CASCADE)
    user=models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    booking_time=models.DateTimeField(null=False)
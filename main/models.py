from django.conf.global_settings import CACHES
from django.db import models
from django.contrib.auth.admin import User
from django_jalali.db import models as jmodels


# Create your models here.

class MorSh(models.Model):

    class Status(models.Choices):
        MELLI =  'M', 'کارت ملی'
        SHENASNAME = 'SH', 'شناسنامه'

    First_Name = models.CharField(max_length=30)
    Last_Name = models.CharField(max_length=40)
    Father_Name = models.CharField(max_length=30)

    status = models.CharField(max_length=2,choices=Status.choices,default=Status.MELLI)

    auther = models.ForeignKey(User,on_delete=SET_NULL,related_name='MorSh')

    date_S = jmodels.jDateTimeField(auto_now_add=True)



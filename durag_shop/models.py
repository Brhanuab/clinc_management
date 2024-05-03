from tokenize import group
from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):


    groups=models.ManyToManyField('auth.group',related_name='cutom_user_group',blank=True,verbose_name='groups')
    user_permissions=models.ManyToManyField('auth.permission',related_name='custem_user_permssion',verbose_name='user permission')
    is_doctor=models.BooleanField(default=False)
    is_manager=models.BooleanField(default=False )
    is_employer=models.BooleanField(default=False)
    is_patient=models.BooleanField(default=False)
    




class branch(models.Model):
    name=models.CharField(max_length=100)
    location=models.CharField(max_length=100)




class manager(models.Model):
    user=models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    branch=models.ForeignKey(branch,on_delete=models.CASCADE)
    


class doctor(models.Model):
    user=models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    branch=models.ForeignKey(branch,on_delete=models.CASCADE)
    

class employer(models.Model):
    user=models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    branch=models.ForeignKey(branch,on_delete=models.CASCADE)


class patient(models.Model):
    user=models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    branch=models.ForeignKey(branch,on_delete=models.CASCADE)



# Create your models here.

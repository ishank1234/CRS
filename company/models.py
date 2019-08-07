from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Company(models.Model):
    c_name=models.CharField(max_length=30)
    c_HR_name = models.CharField(max_length=30)
    c_email=models.CharField(max_length=40)
    c_contact=models.IntegerField()
    c_venue=models.CharField(max_length=30)
    c_date = models.DateField()
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    stu_apply=models.IntegerField(blank=True,null=True)
    stu_select=models.IntegerField(blank=True,null=True)
    def __str__(self):
        return self.c_name
class Drive(models.Model):
    app=models.ForeignKey(Company,on_delete=models.CASCADE)
    stu_Roll=models.IntegerField()
class Select(models.Model):
    com=models.ForeignKey(Company,on_delete=models.CASCADE)
    stu_roll=models.IntegerField()

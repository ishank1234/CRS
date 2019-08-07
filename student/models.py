from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Dept(models.Model):
    name=models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Stu(models.Model):
    d=models.ForeignKey(Dept,on_delete=models.CASCADE)
    Year_Of_Completion = models.IntegerField()
    Roll_number = models.IntegerField(primary_key=True)
    Name = models.CharField(max_length=30)
    Sex = models.CharField(max_length=8)
    DOB = models.DateField()
    Email = models.CharField(max_length=40)
    Contact = models.IntegerField()
    Percentile = models.IntegerField()
    HighSchool = models.IntegerField()
    HighPer = models.IntegerField()
    Intermediate = models.IntegerField()
    InterPer = models.IntegerField()
    user=models.OneToOneField(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.Name

class Both(models.Model):
    comp_id=models.IntegerField()
    stu_id=models.IntegerField()

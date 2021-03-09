from django.db import models
from accounts.models import User
from center.models import Units
# Create your models here.

class StudentsFeedBack(models.Model):
    name = models.ForeignKey(User, blank = True,null= True, on_delete = models.CASCADE)
    purpose = models.CharField(max_length= 100, blank = True, null = True)
    message =  models.TextField(max_length= 355,  blank  = True, null= True)


    def __str__(self):
        return self.name


class Assignment(models.Model):
    name = models.ForeignKey(User, blank = True,null= True, on_delete = models.CASCADE)
    handin = models.FileField ()
    date = models.DateTimeField(auto_now_add= True)


    def __str__(self):
        return self.name


class Retake(models.Model):
    name = models.ForeignKey(User, blank = True,null= True, on_delete = models.CASCADE)
    unit = models. ForeignKey(Units, blank= True, null =  True, on_delete = models.CASCADE)
    date = models.DateTimeField(auto_now_add= True) 


    def __str__(self):
        return self.name



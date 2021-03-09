from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    name                    = models.CharField(max_length=100, blank=True, null=True)
    is_student              = models.BooleanField('student status', default=False)
    is_teacher              = models.BooleanField('teacher status', default=False)
    is_finance              = models.BooleanField('finance status', default=False)
    is_head_of_department   = models.BooleanField('head of department  status', default=False)



    def __str__(self):
        return self.name

    
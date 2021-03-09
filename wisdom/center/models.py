from django.db import models
from accounts.models import User

# Create your models here.
class Department(models.Model):
    department      = models.CharField(max_length= 30, null= True, blank = True)
    id_number       = models.CharField(max_length= 20 ,  blank = True, unique= True, primary_key= True)

    def __str__(self):
        return self.department
 

class HOD(models.Model):
    user             =  models.ForeignKey(User,null = True, blank = True, on_delete  = models.CASCADE)
    department       = models.ForeignKey(Department, null = True, blank = True, on_delete  = models.CASCADE)
    id_number        = models.CharField(max_length= 20 ,  blank = True, unique= True, primary_key= True)


    def __str__(self):
        return self.user

 
class Course(models.Model):
    course          = models.CharField(max_length= 20 , null= True, blank = True)
    id_number       = models.CharField(max_length= 20 , blank = True, unique= True, primary_key= True)


    def __str__(self):
        return self.course


class Units(models.Model):
    course          = models.ForeignKey(Course, blank= True, null = True, on_delete = models.CASCADE)
    units           = models.CharField(max_length= 20 , null= True, blank = True)
    id_number       = models.CharField(max_length= 20 ,  blank = True, unique= True, primary_key= True)


    def __str__(self):
        return self.units



class Teacher(models.Model):
    user            = models.ForeignKey(User, null = True, blank = True, on_delete  = models.CASCADE)
    age             = models.IntegerField()
    tel             = models.CharField(max_length= 255 , blank = True, null = True)
    email           = models.EmailField()
    address         = models.TextField()
    department      = models.ForeignKey(Department, null = True, blank = True, on_delete  = models.CASCADE)
    report_to       = models.ForeignKey(HOD,null = True, blank = True, on_delete  = models.CASCADE)
    units           = models.ForeignKey(Units,null = True, blank = True, on_delete  = models.CASCADE)
    id_number       = models.CharField(max_length= 20 ,  blank = True, unique= True, primary_key= True)


    def __str__(self):
        return self.user



class Finance(models.Model):

    ROLES = [('Accountant', 'Accountant'),('Cashier', 'Cashier')]

    user            = models.ForeignKey(User, null = True, blank = True, on_delete  = models.CASCADE)
    role            = models.CharField(max_length= 255 , blank = True, null = True, choices= ROLES)
    id_number       = models.CharField(max_length= 20 , blank = True, unique= True, primary_key= True)


  


class Student(models.Model):
    user            = models.ForeignKey(User, null = True, blank = True, on_delete  = models.CASCADE)
    age             = models.IntegerField()
    tel             = models.CharField(max_length= 255 , blank = True, null = True)
    email           = models.EmailField()
    parent          = models.CharField(max_length= 255 , blank = True, null = True)
    parents_contact = models.CharField(max_length= 255 , blank = True, null = True)
    email_parent    = models.EmailField()
    address         = models.TextField()
    department      = models.ForeignKey(Department, null = True, blank = True, on_delete  = models.CASCADE)
    report_to       = models.ForeignKey(HOD,null = True, blank = True, on_delete  = models.CASCADE)
    units           = models.ForeignKey(Units,null = True, blank = True, on_delete  = models.CASCADE)
    id_number       = models.CharField(max_length= 20 ,  blank = True, unique= True, primary_key= True)


    def __str__(self):
        return self.user.name



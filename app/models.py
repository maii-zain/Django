from django.db import models

class Student(models.Model):
    # id=models.AutoField(primary_key=True)
    f_name=models.CharField(max_length=50)
    l_name=models.CharField(max_length=50)
    age=models.IntegerField()
    
class Person(models.Model):
    st_name=models.CharField(max_length=50)   
    nd_name=models.CharField(max_length=50)
    email=models.EmailField(max_length=254)
    password=models.CharField(max_length=50)
# Create your models here.

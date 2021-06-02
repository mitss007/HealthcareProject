from django.db import models

# Create your models here.
class User(models.Model):
    fname=models.CharField(max_length=100)
    lname=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    gender=models.CharField(max_length=100, default=0)
    phone=models.CharField(max_length=100)
    address=models.TextField()

    def __str__(self):
        return self.fname

class Make_appoint(models.Model):
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    date=models.CharField(max_length=100)
    dept=models.CharField(max_length=100, default=0)
    phone=models.CharField(max_length=100)
    message=models.TextField()


    def __str__(self):
        return self.name
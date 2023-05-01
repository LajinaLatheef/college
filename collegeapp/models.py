from django.db import models

# Create your models here.

class Data(models.Model):

    name=models.CharField(max_length=250)
    dob=models.DateField()
    age=models.IntegerField()
    phonenumber=models.IntegerField()
    mailid=models.EmailField()
    address=models.TextField(max_length=250)


    def __str__(self):
        return self.name

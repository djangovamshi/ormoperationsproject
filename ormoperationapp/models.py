from django.db import models

# Create your models here.
class Employee(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    salary = models.IntegerField()
    mobile = models.BigIntegerField()
    address = models.CharField(max_length=50)

    def __str__(self):
        return self.firstname

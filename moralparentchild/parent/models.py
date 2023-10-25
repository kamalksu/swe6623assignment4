from django.db import models

# Create your models here.

class Parent(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    zip_code = models.CharField(max_length=20)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    profession = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    email = models.CharField(max_length=60)
    desription = models.CharField(max_length=400)
    possible_funding = models.IntegerField(null=True)
    background_cheking = models.BooleanField(default=False)
    background_check_comment = models.CharField(max_length=400, null=True)
    application_date = models.DateField(null=True)
    application_approval_date = models.DateField(null=True)
    isRemoved = models.BooleanField(default=False)


    def __str__(self):
        return f"{self.firstname} {self.lastname}"
from django.db import models

# Create your models here.

class Child(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    zip_code = models.CharField(max_length=20)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    phone = models.CharField(max_length=50)
    email = models.CharField(max_length=60)
    date_of_birth = models.DateField(null=True)
    school_name = models.CharField(max_length=200)
    school_address = models.CharField(max_length=200)
    school_zip = models.CharField(max_length=20)
    desription = models.CharField(max_length=400)
    fund_request_amount = models.IntegerField(null=True)
    fund_request_months = models.IntegerField(null=True)
    fund_approved_amount = models.IntegerField(null=True)
    fund_approved_months = models.IntegerField(null=True)    
    background_cheking = models.BooleanField(default=False)
    background_check_comment = models.CharField(max_length=400)
    application_date = models.DateField(null=True)
    application_approval_date = models.DateField(null=True)
    isRemoved = models.BooleanField(default=False)


    def __str__(self):
        return f"{self.firstname} {self.lastname}"
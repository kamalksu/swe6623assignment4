from django.db import models
import datetime
# Create your models here.

class Child(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    address = models.CharField(max_length=255, blank=True)
    zip_code = models.CharField(max_length=20, blank=True)
    state = models.CharField(max_length=100, blank=True)
    country = models.CharField(max_length=100, blank=True)
    phone = models.CharField(max_length=50)
    email = models.CharField(max_length=60)
    date_of_birth = models.DateField(null=True, blank=True)
    photo = models.ImageField(null=True, blank=True, upload_to="documents/")
    school_name = models.CharField(max_length=200, blank=True)
    school_address = models.CharField(max_length=200, blank=True)
    school_zip = models.CharField(max_length=20, blank=True)
    desription = models.TextField(max_length=800, blank=True)
    fund_request_amount = models.IntegerField(null=True, blank=True)
    fund_request_months = models.IntegerField(null=True, blank=True)
    fund_approved_amount = models.IntegerField(null=True, blank=True)
    fund_approved_months = models.IntegerField(null=True, blank=True)    
    background_cheking = models.BooleanField(default=False)
    background_check_comment = models.CharField(max_length=400, null=True, blank=True)
    application_date = models.DateField(null=True, blank=True, default=datetime.date.today)
    application_approval_date = models.DateField(null=True, blank=True)
    isRemoved = models.BooleanField(default=False)
    login_id = models.CharField(max_length=100, null=True, blank=True)
    supporting_document1 = models.ImageField(null=True, blank=True, upload_to="documents/")
    supporting_document2 = models.ImageField(null=True, blank=True, upload_to="documents/")


    def __str__(self):
        return f"{self.firstname} {self.lastname}"
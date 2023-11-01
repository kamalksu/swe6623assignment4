from django.db import models

# Create your models here.

class Parent(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    address = models.CharField(max_length=255, blank=True)
    zip_code = models.CharField(max_length=20, blank=True)
    state = models.CharField(max_length=100, blank=True)
    country = models.CharField(max_length=100, blank=True)
    profession = models.CharField(max_length=50, blank=True)
    phone = models.CharField(max_length=50)
    email = models.CharField(max_length=60)
    desription = models.CharField(max_length=400, blank=True)
    possible_funding = models.IntegerField(null=True, blank=True)
    background_cheking = models.BooleanField(default=False)
    background_check_comment = models.CharField(max_length=400, null=True, blank=True)
    application_date = models.DateField(null=True, blank=True)
    application_approval_date = models.DateField(null=True, blank=True)
    isRemoved = models.BooleanField(default=False)
    login_id = models.CharField(max_length=100, blank=True)


    def __str__(self):
        return f"{self.firstname} {self.lastname}"
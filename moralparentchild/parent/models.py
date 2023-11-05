from django.db import models
import datetime

#from child.models import Child

# Create your models here.

class Parent(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    address = models.CharField(max_length=255, blank=True)
    zip_code = models.CharField(max_length=20, blank=True)
    state = models.CharField(max_length=100, blank=True)
    country = models.CharField(max_length=100, blank=True)
    profession = models.CharField(max_length=50, blank=True)
    photo = models.ImageField(null=True, blank=True, upload_to="documents/")
    phone = models.CharField(max_length=50)
    email = models.CharField(max_length=60)
    desription = models.TextField(max_length=400, blank=True)
    possible_funding = models.IntegerField(null=True, blank=True)
    background_cheking = models.BooleanField(default=False)
    background_check_comment = models.CharField(max_length=400, null=True, blank=True)
    application_date = models.DateField(null=True, blank=True, default=datetime.date.today)
    application_approval_date = models.DateField(null=True, blank=True)
    isRemoved = models.BooleanField(default=False)
    login_id = models.CharField(max_length=100, blank=True)
    supporting_document1 = models.ImageField(null=True, blank=True, upload_to="documents/")
    supporting_document2 = models.ImageField(null=True, blank=True, upload_to="documents/")


    def __str__(self):
        return f"{self.firstname} {self.lastname}"
    


class ListofMoralParent(models.Model):
    possible_funding = models.IntegerField(null=True, blank=True)
    parent_id = models.ForeignKey(Parent, default=1, verbose_name="Parent Name", on_delete=models.SET_DEFAULT)
    background_checked = models.BooleanField(null=True, default=False)
    approved = models.BooleanField(null=True, default=False)
    comments = models.TextField(max_length=400, null=True, blank=True )
    child_id = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return f"{self.parent_id}"


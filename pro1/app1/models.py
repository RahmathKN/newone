from django.db import models

# Create your models here.
class Client(models.Model):
    client_name =models.CharField(max_length=50)
    client_phone = models.CharField(max_length=12)
    client_email = models.EmailField(max_length=70)
    # client_address=models.CharField(max_length=100)
    client_msg=models.CharField(max_length=100)
    c_username=models.CharField(max_length=50)
    c_password=models.CharField(max_length=50)
    # client_status=models.CharField(max_length=50,default='pending')
class Admin(models.Model):
    loginname=models.CharField(max_length=50)
    password=models.CharField(max_length=50)
class Project(models.Model):
    proj_name=models.CharField(max_length=50)
    proj_details=models.CharField(max_length=200)
    proj_img=models.FileField()
    proj_date=models.CharField(max_length=50)
    proj_budjet=models.IntegerField()
    proj_dur=models.IntegerField()
# class Login(models.Model):
#     username=models.CharField(max_length=50)
#     password=models.CharField(max_length=50)

from django.db import models

# Create your models here.
class SignupDetails(models.Model):
  username = models.CharField(max_length=100)
  fname = models.CharField(max_length=30)
  lname = models.CharField(max_length=30)
  Email = models.EmailField(max_length=50)
  pass1 = models.CharField(max_length=50)
  pass2 = models.CharField(max_length=50)
      

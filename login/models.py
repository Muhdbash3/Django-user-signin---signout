from django.db import models

# Create your models here.
class SignupDetails(models.Model):
  username = models.CharField(max_length=100)
  firstName = models.CharField(max_length=30)
   lastName = models.CharField(max_length=30)
     Email = models.EmailField(max_length=50)
      password1 = models.CharField(max_length=50)
      password2 = models.CharField(max_length=50)
      

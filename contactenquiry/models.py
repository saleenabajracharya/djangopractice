from django.db import models
class contactEnquiry(models.Model):
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=60)
    subject=models.CharField(max_length=50)
    message=models.TextField()

# Create your models here.

from django.db import models

# Create your models here.
class Contacts(models.Model):
    phone_number = models.CharField(max_length=50)
    address = models.CharField(max_length=255)
    email = models.EmailField()

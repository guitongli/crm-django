from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.deletion import CASCADE
# Create your models here.
#User = get_user_model()

class Client(models.Model):
    client_name = models.CharField(max_length=20)
    
class User(AbstractUser):
    pass

class Order(models.Model):
    REGION_CHOICES = (
        ('UK', 'UK'),
        ('USA', 'USA'),
        ('EU', 'EU')
    )
    product= models.CharField(max_length=20)
    brand = models.CharField(max_length=20)
    EK = models.FloatField(default=0)
    Quantity = models.IntegerField(default=0)
    shipment_cost= models.FloatField(default=0)
    asin = models.CharField(blank=True, null=True, max_length=20)
    project_number = models.CharField(max_length=20)
    tariff = models.FloatField(default=0)
    fba = models.FloatField(default=0)
    sold_per_day = models.IntegerField(default=0)
    client_region = models.CharField(choices=REGION_CHOICES, max_length=100)
    special_files = models.FileField(blank=True, null=True)
    client = models.ForeignKey("Client", max_length=20, on_delete=models.SET_NULL, null=True)

     
class Agent(models.Model):
    user = models.OneToOneField(User, on_delete=CASCADE)

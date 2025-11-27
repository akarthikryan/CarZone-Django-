from django.db import models

# Create your models here.
class Car(models.Model):
    car_name = models.CharField(max_length=255)
    car_model = models.CharField(max_length=255)
    car_photo = models.ImageField(upload_to='cars/%Y/%m/%d/')
    address = models.CharField(max_length=255)
    kilometers_driven = models.IntegerField()
    fuel_type = models.CharField(max_length=100)
    transmission_type = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    color = models.CharField(max_length=100)
    created_date = models.DateTimeField(auto_now_add=True)

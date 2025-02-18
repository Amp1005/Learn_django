from django.db import models
import django.utils.timezone

# class Student(models.Model):
#     id = models.AutoField(primary_key=True)  # If needed, explicitly define this
#     name = models.CharField(max_length=100)
#     age = models.IntegerField() 
#     address = models.TextField()
#     email = models.EmailField()
#     image = models.ImageField()
#     file = models.FileField(upload_to='uploads/')  # Ensure this is correctly set

class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField(default=18)
    email = models.EmailField(null=True,blank=True)
    address = models.CharField(max_length=255, default="Unknown Address")  # Add a default value

    def __str__(self):
        return self.name

class Car(models.Model):
    car_name = models.CharField(max_length=100)  # Make sure this matches
    speed = models.IntegerField()

    def __str__(self):
        return f"{self.car_name} - {self.speed} km/h"
    
    

# Create your models here.
from django.db import models

# This model represents a pet listing
class Pet(models.Model):
    name = models.CharField(max_length=100)  # Pet name
    age = models.IntegerField()              # Pet age
    breed = models.CharField(max_length=100) # Pet breed
    photo = models.ImageField(upload_to='pet_photos/')  # Photo of pet
    approved = models.BooleanField(default=False)  # Admin approval

    def _str_(self):
        return self.name

# Contact form submissions
class Contact(models.Model):
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)   # Person name
    email = models.EmailField()               # Email
    message = models.TextField()              # Message
    created_at = models.DateTimeField(auto_now_add=True)
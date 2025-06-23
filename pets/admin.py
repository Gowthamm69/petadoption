# Register your models here.
from django.contrib import admin
from .models import Pet, Contact

# This will allow us to manage Pet and Contact from admin panel
admin.site.register(Pet)
admin.site.register(Contact)
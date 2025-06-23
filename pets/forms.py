from django import forms
from .models import Contact

# Contact Form for users
class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'message']
# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from .models import Pet
from .forms import ContactForm

# Show only approved pets
def home(request):
    pets = Pet.objects.filter(approved=True)
    return render(request, 'pets/home.html', {'pets': pets})

# Show details + contact form
def pet_detail(request, pet_id):
    pet = get_object_or_404(Pet, pk=pet_id)
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save(commit=False)
            contact.pet = pet
            contact.save()
            return render(request, 'pets/thanks.html')
    else:
        form = ContactForm()
    return render(request, 'pets/pet_detail.html', {'pet': pet, 'form': form})
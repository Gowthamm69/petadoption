from pets.models import Pet
Pet.objects.create(name="Max", age=5, breed="Labrador", photo="pet_photos/max.jpg", approved=True)
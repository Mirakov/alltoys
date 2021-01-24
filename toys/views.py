from django.shortcuts import render
from toys.models import Toy
from django.utils import timezone

def dashboard(request):
    return render(request, "toys/dashboard.html", context={"welcome_text": "Welcome to AllToys!"})

def get_toys(request):
    toys = Toy.objects.all()
    toys = toys.filter(created_at__year=timezone.now().year)
    return render(request, "toys/toys.html", context={"toys": toys})


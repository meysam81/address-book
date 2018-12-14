from django.shortcuts import render
from .models import Address

# Create your views here.
def index(request):
    addresses = Address.objects
    return render(request, 'index.html', {'addresses': addresses})

def add(request):
    return render(request, 'add.html')

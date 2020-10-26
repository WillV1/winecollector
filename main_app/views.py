from django.shortcuts import render 
from .models import Wine

# Create your views here.


def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def wines_index(request):
    wines = Wine.objects.all()
    return render(request, 'wines/index.html', {'wines': wines})

# def wines_about(request):
#     return render(request, 'wines/about.html')
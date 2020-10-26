from django.shortcuts import render
from django.http import HttpResponse 
# from .models import wines

# Create your views here.


def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

# def wines_index(request):
#     return render(request, 'wines/index.html', {'wines': wines})
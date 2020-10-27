from django.shortcuts import render 
# from .models import Producer
# from .models import Wine

# Create your views here.


def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

# def producers_index(request):
#     producers = Producer.objects.all()
#     return render(request, 'producers/index.html', {'producers': producers})

# def producers_details(request, wine_id):
#     producer = Producer.objects.get(id=producer_id)
#     return render(request, 'producers/detail.html', {'producer': producer})

# def wines_index(request):
#     wines = Wine.objects.all()
#     return render(request, 'wines/index.html', {'wines': wines})

# def wines_details(request, wine_id):
#     wine = Wine.objects.get(id=wine_id)
#     return render(request, 'wines/detail.html', {'wine': wine})
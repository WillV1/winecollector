from django.shortcuts import render, redirect 
from .models import Producer, Distributor
from .forms import WineForm

# Create your views here.


def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def producers_index(request):
    producers = Producer.objects.all()
    return render(request, 'producers/index.html', {'producers': producers})

def producers_details(request, producer_id):
    producer = Producer.objects.get(id=producer_id)
    available_distributors = Distributor.objects.exclude(id__in = producer.distributors.all().values_list('id'))
    wine_form = WineForm()
    return render(request, 'producers/detail.html', {
        'producer': producer,
        'wine_form': wine_form,
        'distributors': available_distributors
        })

def add_wine(request, producer_id):
    form = WineForm(request.POST)

    if form.is_valid():
        new_wine = form.save(commit=False)
        new_wine.producer_id = producer_id
        new_wine.save()

    return redirect('producers_details', producer_id)

def assoc_distributor(request, producer_id, distributor_id):
    # Note that you can pass a toy's id instead of the whole object
    Producer.objects.get(id=producer_id).distributors.add(distributor_id)
    return redirect('producers_details', producer_id=producer_id)

def remove_distributor(request, producer_id, distributor_id):
    Producer.objects.get(id=producer_id).distributors.remove(distributor_id)
    return redirect('producers_details', producer_id=producer_id)

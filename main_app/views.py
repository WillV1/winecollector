from django.shortcuts import render, redirect 
from .models import Producer, Distributor
from .forms import WineForm, ProducerForm

# Create your views here.

#-------STATIC

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

#------PRODUCERS

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

def add_producer(request):
    if request.method == 'POST':
        producer_form = ProducerForm(request.POST)
        if producer_form.is_valid():
            new_producer = producer_form.save(commit=False)
            new_producer.save()
            return redirect('producers_details', new_producer.id)
    else: 
        form = ProducerForm()
        context = {'form': form}
        return render(request, 'producers/new.html', context)

def delete_producer(request, producer_id):
    Producer.objects.get(id=producer_id).delete()

    return redirect('producers_index')

def edit_producer(request, producer_id):
    producer = Producer.objects.get(id=producer_id)

    if request.method == 'POST':
        producer_form = ProducerForm(request.POST, instance=producer)
        if producer_form.is_valid():
            updated_producer = producer_form.save()
            return redirect('producers_detail', updated_producer.id)
    else: 
        form = ProducerForm(instance=cat)
        context = {'form': form}
        return render(request, 'producers/edit.html', context)


#-----ADD WINE

def add_wine(request, producer_id):
    form = WineForm(request.POST)

    if form.is_valid():
        new_wine = form.save(commit=False)
        new_wine.producer_id = producer_id
        new_wine.save()

    return redirect('producers_details', producer_id)

#------DISTRIBUTOR

def assoc_distributor(request, producer_id, distributor_id):
    # Note that you can pass a toy's id instead of the whole object
    Producer.objects.get(id=producer_id).distributors.add(distributor_id)
    return redirect('producers_details', producer_id=producer_id)

def remove_distributor(request, producer_id, distributor_id):
    Producer.objects.get(id=producer_id).distributors.remove(distributor_id)
    return redirect('producers_details', producer_id=producer_id)

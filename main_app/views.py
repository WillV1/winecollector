from django.shortcuts import render, redirect 
from .models import Producer, Distributor
from .forms import WineForm, ProducerForm, DistributorForm
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

# Create your views here.

#-------STATIC

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

#-------SIGNUP

def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('producers_index')
    else: 
        error_message = 'Invalid sign up - try again'
        form = UserCreationForm()
        context = {'form': form, 'error_message': error_message}
        return render(request, 'registration/signup.html', context)

#------PRODUCERS

@login_required
def producers_index(request):
    if request.method == 'POST':
        producer_form = ProducerForm(request.POST)
        if producer_form.is_valid():
            new_producer = producer_form.save(commit=False)
            new_producer.user = request.user
            new_producer.save()
            return redirect('producers_index')
    producers = Producer.objects.filter(user=request.user)
    producer_form = ProducerForm()
    context = {'producers': producers, 'producer_form': producer_form}
    return render(request, 'producers/index.html', context)

@login_required
def producers_details(request, producer_id):
    producer = Producer.objects.get(id=producer_id)
    available_distributors = Distributor.objects.exclude(id__in = producer.distributors.all().values_list('id'))
    wine_form = WineForm()
    return render(request, 'producers/detail.html', {
        'producer': producer,
        'wine_form': wine_form,
        'distributors': available_distributors
        })

@login_required
def add_producer(request):
    if request.method == 'POST':
        producer_form = ProducerForm(request.POST)
        if producer_form.is_valid():
            new_producer = producer_form.save(commit=False)
            new_producer.user = request.user
            new_producer.save()
            return redirect('producers_details', new_producer.id)
    else: 
        form = ProducerForm()
        context = {'form': form}
        return render(request, 'producers/new.html', context)

@login_required
def delete_producer(request, producer_id):
    Producer.objects.get(id=producer_id).delete()

    return redirect('producers_index')

@login_required
def edit_producer(request, producer_id):
    producer = Producer.objects.get(id=producer_id)

    if request.method == 'POST':
        producer_form = ProducerForm(request.POST, instance=producer)
        if producer_form.is_valid():
            updated_producer = producer_form.save()
            return redirect('producers_details', updated_producer.id)
    else: 
        form = ProducerForm(instance=producer)
        context = {'form': form}
        return render(request, 'producers/edit.html', context)


#-----ADD WINE

@login_required
def add_wine(request, producer_id):
    form = WineForm(request.POST)

    if form.is_valid():
        new_wine = form.save(commit=False)
        new_wine.producer_id = producer_id
        new_wine.save()

    return redirect('producers_details', producer_id)

#------DISTRIBUTOR

@login_required
def add_distributor(request):
    if request.method == 'POST':
        distributor_form = DistributorForm(request.POST)
        if distributor_form.is_valid():
            new_distributor = distributor_form.save(commit=False)
            new_distributor.save()
            return redirect('producers_index')
    else: 
        form = DistributorForm()
        context = {'form': form}
        return render(request, 'distributors/new.html', context)

@login_required
def assoc_distributor(request, producer_id, distributor_id):
    # Note that you can pass a toy's id instead of the whole object
    Producer.objects.get(id=producer_id).distributors.add(distributor_id)
    return redirect('producers_details', producer_id=producer_id)

@login_required
def remove_distributor(request, producer_id, distributor_id):
    Producer.objects.get(id=producer_id).distributors.remove(distributor_id)
    return redirect('producers_details', producer_id=producer_id)

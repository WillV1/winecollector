from django import forms
from .models import Wine, Producer, Distributor

class WineForm(forms.ModelForm):
    class Meta:
        model = Wine
        fields = ['name', 'size', 'price']

class ProducerForm(forms.ModelForm):
    class Meta:
        model = Producer
        fields = ('name', 'country', 'region', 'grape', 'description')

class DistributorForm(forms.ModelForm):
    class Meta:
        model = Distributor
        fields = ('name', 'country', 'website')
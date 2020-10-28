from django.contrib import admin
from .models import Producer, Wine, Distributor

# Register your models here.
admin.site.register(Producer)
admin.site.register(Wine)
admin.site.register(Distributor)
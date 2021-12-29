from Automobiles.views import automobile
from Appliances.views import appliance
from django.shortcuts import render

from .models import Slider,Stock
from Appliances.models import Appliance
from Automobiles.models import Automobile
# Create your views here.
def index(request):
    sliders = Slider.objects.all()
    stokes = Stock.objects.all()
    appliances = Appliance.objects.all()
    automobiles = Automobile.objects.all()
    context ={
        'sliders' :sliders,
        'automobiles':automobiles,
        'appliances':appliances,
        'stokes':stokes
    }
    return render(request, 'Landn/index.html', context)
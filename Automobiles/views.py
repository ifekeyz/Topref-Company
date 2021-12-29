from django.shortcuts import get_object_or_404,render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .models import Automobile
# Create your views here.
def index(request):
    automobiles = Automobile.objects.all()
    context ={
       'automobiles': automobiles
    }
    return render(request, 'Auto/index.html',context)

def automobile(request, automobile_id):
    automobile = get_object_or_404(Automobile, pk=automobile_id)
    context={
        'automobile':automobile
    }
    return render(request, 'Auto/automobile.html', context)
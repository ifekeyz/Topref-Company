from django.shortcuts import get_object_or_404,render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .models import Appliance
# Create your views here.
def index(request):
    # context={
    #     'name': 'feranmi'
    # }
    # return render(request, 'Home/index.html',context)
    appliances = Appliance.objects.all()
    context = {
        'appliances': appliances
    }
    return render(request, 'Home/index.html', context)

def appliance(request, appliance_id):
    appliance = get_object_or_404(Appliance, pk=appliance_id)
    context={
        'appliance':appliance
    }
    return render(request, 'Home/appliance.html', context)
from django.shortcuts import render,redirect
from . models import Contact

# Create your views here.
def index(request):

    if request.method=="POST":
        contact = Contact()
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        contact.name=name
        contact.email=email
        contact.subject=subject
        contact.message=message
        contact.save()
        return redirect('index')
    return render(request, 'Contact/index.html')
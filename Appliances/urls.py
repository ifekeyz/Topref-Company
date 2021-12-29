from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='appliances'),
    path('<int:appliance_id>', views.appliance, name='appliance')
]

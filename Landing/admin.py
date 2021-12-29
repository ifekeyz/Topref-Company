from django.contrib import admin

# Register your models here.
from .models import Slider,Stock

admin.site.register(Slider)
admin.site.register(Stock)
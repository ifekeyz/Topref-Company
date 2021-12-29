from django.db import models
from datetime import datetime

# Create your models here.
class Automobile(models.Model):
    carName = models.CharField(max_length=20,blank=True)
    image = models.ImageField(upload_to='photos/%Y/%m/%d',blank=True)
    image1 = models.ImageField(upload_to='photos/%Y/%m/%d',blank=True)
    image2 = models.ImageField(upload_to='photos/%Y/%m/%d',blank=True)
    image3 = models.ImageField(upload_to='photos/%Y/%m/%d',blank=True)
    image4 = models.ImageField(upload_to='photos/%Y/%m/%d',blank=True)
    price = models.CharField(max_length=20,blank=True)
    brief = models.TextField(default=True)
    maker = models.CharField(max_length=20, blank=True)
    status = models.CharField(max_length=20)
    location = models.CharField(max_length=20,blank=True)
    color = models.CharField(max_length=20,blank=True)
    brandYear = models.CharField(max_length=20,blank=True)
    gradeType = models.CharField(max_length=20)
    list_date = models.DateTimeField(default=datetime.now, blank=True)
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.carName
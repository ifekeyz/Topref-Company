from django.db import models
from datetime import datetime

# Create your models here.
class Appliance(models.Model):
    itemName = models.CharField(max_length=20)
    image = models.ImageField(upload_to='photos/%Y/%m/%d')
    image1 = models.ImageField(upload_to='photos/%Y/%m/%d')
    image2 = models.ImageField(upload_to='photos/%Y/%m/%d')
    image3 = models.ImageField(upload_to='photos/%Y/%m/%d')
    image4 = models.ImageField(upload_to='photos/%Y/%m/%d')
    price = models.CharField(max_length=20)
    brief = models.TextField()
    maker = models.CharField(max_length=20)
    status = models.CharField(max_length=20)
    color = models.CharField(max_length=20)
    gradeType = models.CharField(max_length=20)
    list_date = models.DateTimeField(default=datetime.now)
    is_published = models.BooleanField()
    
    def __str__(self):
        return self.itemName
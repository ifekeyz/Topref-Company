from django.db import models

# Create your models here.
class Slider(models.Model):
    tag = models.CharField(max_length=20,blank=True)
    image1 = models.ImageField(upload_to='photos/%Y/%m/%d',blank=True)
    image2 = models.ImageField(upload_to='photos/%Y/%m/%d',blank=True)
    is_needed = models.BooleanField(default=True)
    def __str__(self):
        return self.tag

        

class Stock(models.Model):
    tag = models.CharField(max_length=20, blank=True)
    image = models.ImageField(upload_to='photos/%Y/%m/%d',blank=True)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d',blank=True)
    message = models.TextField(blank=True)
    is_needed = models.BooleanField(default=True)
    def __str__(self):
        return self.tag


from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=50, blank=True)
    email = models.EmailField(blank=True)
    subject = models.CharField(max_length=50, blank=True)
    message = models.TextField(blank=True)

    def __str__(self):
        return self.name


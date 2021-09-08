from django.db import models


# Create your models here.
class Ocr(models.Model):
    # name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images/')

   


class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    message = models.TextField()    

    def __str__(self):
        return self.name
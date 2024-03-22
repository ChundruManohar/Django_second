from django.db import models
import datetime 
# Create your models here.


class Contact(models.Model):
    first_name = models.CharField(max_length=200)
    Last_name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length = 200)
    is_active = models.BooleanField(default = False)
    created_at = models.DateTimeField(default = datetime.datetime.now())
    
    def __str__(self):
        return f'{self.email} {self.state}'
    
    
class About(models.Model):
    title= models.CharField(max_length=200)
    description =models.TextField()
    image = models.ImageField(upload_to='about')
    
    
    def __str__(self) -> str:
        return self.title
    
    
from django.db import models
from django.urls import reverse


# Create your models here.

class Portfolio(models.Model):
    name=models.CharField(max_length=100)
    title=models.CharField(max_length=100,blank=True)
    location=models.TextField(max_length=250,blank=True)
    desc=models.TextField(max_length=250,blank=True)
    image=models.ImageField(upload_to='images/pics',blank=True,null=True)
    email=models.EmailField()
    url=models.URLField(blank=True)


    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail',kwargs={
            'blog_id': self.id
        })





class Blog(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100, blank=True)
    location = models.TextField(max_length=250, blank=True)
    desc = models.TextField(max_length=250, blank=True)
    email = models.EmailField()

    def __str__(self):
        return self.name
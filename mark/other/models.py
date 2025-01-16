from django.db import models
from django.db import models
from django.urls import reverse
# Create your models here.

from django.db import models
from django.urls import reverse
# Create your models here.
class Service(models.Model):
    image = models.ImageField(upload_to='media/services/')
    heading = models.CharField(max_length=50)
    sub_heading = models.CharField(max_length=150)
    slug = models.SlugField(unique=True)
    introduction = models.TextField()
    what_is= models.TextField()
    process = models.TextField()
    benefits= models.TextField()
    example= models.TextField()

    
    url = models.URLField(max_length=200)
    
    def __str__(self):
        return self.heading
    def url(self):
        return reverse('service',kwargs={'slug' : self.slug})
    

class Project(models.Model):
    
    name = models.CharField(max_length=50)
    details = models.CharField(max_length=120)
    image = models.ImageField(upload_to='media/project_images')
    more = models.TextField(blank=True,null=True)
    show_on_home = models.BooleanField(default=True)
    
    def __str__(self):
        return self.name


class Blog(models.Model):
    image = models.ImageField( upload_to='media/blog/')
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True)
    short_details = models.TextField()
    create = models.DateTimeField(auto_now=True)
    blog_link = models.URLField(max_length=500)
    
    def __str__(self):
        return self.title
    
    def url(self):
        return reverse('blog_detail', args=[self.slug])

class Staff(models.Model):
    name = models.CharField(max_length=15)
    details = models.CharField(max_length=500)
    image = models.ImageField(upload_to='media/staff_images/')
    Facebook = models.CharField(max_length=150)
    linkedin = models.CharField(max_length=150)
    mail = models.CharField(max_length=150)
    
    show_on_home = models.BooleanField(default=True)
    
    def __str__(self):
        return self.name
    
    

class Contact(models.Model):
    mobile = models.CharField(blank=True,max_length=100)
    telephone = models.CharField(blank=True,max_length=100)
    whatsapp = models.CharField(blank=True,max_length=100)
    email = models.EmailField(blank=True,max_length=100)
    address = models.TextField(blank=True)
    facebook = models.URLField(blank=True,max_length=200)
    twiter = models.URLField(blank=True,max_length=200)
    linkedin = models.URLField(blank=True,max_length=200)
    instagram = models.URLField(blank=True,max_length=200)



class Message(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    message = models.TextField()
    
    created = models.DateField(auto_now=True)
    
    def __str__(self):
        return self.name
    
    
    
class Review(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='media/review/')
    review = models.TextField()
    email = models.EmailField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name
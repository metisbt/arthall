from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse



class Category(models.Model):
    name = models.CharField(max_length = 255)

    def __str__(self):
        return self.name

class Creation(models.Model):
    title = models.CharField(max_length = 255)
    content = models.TextField()
    image = models.ImageField(upload_to='art/',default='art/default.jpg')
    category = models.ManyToManyField(Category)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    status = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    published_date = models.DateTimeField(null=True)

    class Meta:

        ordering = ['-created_date']

    def __str__ (self):
        return self.title
    
class Exhibition(models.Model):
    userid = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length = 255)
    category = models.ManyToManyField(Category)
    proved = models.BooleanField(default=False)
    date = models.DateTimeField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:

        ordering = ['-created_date']

    def __str__ (self):
        return self.name
    
class Teaching(models.Model):
    userid = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length = 255)
    subject = models.CharField(max_length = 255)
    category = models.ManyToManyField(Category)
    proved = models.BooleanField(default=False)
    date = models.DateTimeField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:

        ordering = ['-created_date']

    def __str__ (self):
        return self.name
    
class RegisterExhibition(models.Model):
    userid = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.ForeignKey(Exhibition, on_delete=models.SET_NULL, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:

        ordering = ['-created_date']

    def __str__ (self):
        return self.name
from django.db import models

# Create your models here.


class Author (models.Model):
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    birth_day = models.DateField()
    history =  models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=False, verbose_name="If the autor is working")

    def __str__(self):
        return (self.name+' '+ self.last_name)

class Book(models.Model):
    titule = models.CharField(max_length=150)
    summary = models.TextField()
    date_created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.titule
    

class Editorial(models.Model):
    name = models.CharField(max_length=150)
    genre = models.CharField(max_length=50)
    summary = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    

    
        
        


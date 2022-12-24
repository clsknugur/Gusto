from django.db import models
from django.core.validators import MaxLengthValidator,MinLengthValidator 
# Create your models here.

class Restourant(models.Model):
    name=models.CharField(max_length=100)
    adress=models.CharField(max_length=250)
    opening_hours=models.CharField(max_length=150)
    reservations=models.IntegerField()

    def __str__(self):
     return self.name



class Menu(models.Model):
     food_types = (
          ('BREAKFASTSTARTERS' , 'BREAKFASTSTARTERS'),
          ('MAIN COURSE' , 'MAIN COURSE'),
          ('DINNER', 'DINNER'),
          ('DESSERTS', 'DINNER'),         
)
     name=models.CharField(max_length=100) 
     price=models.DecimalField(max_digits=8,decimal_places=2)
     description=models.TextField(validators=[MinLengthValidator(10)])
     food_type=models.CharField(max_length=30,choices=food_types)
     restoran=models.ManyToManyField(Restourant)
     def __str__(self):
        return self.name

    



class Person(models.Model):
    genders=(
        ('M','Male'),
        ('F','Female'),
    )

    duty_types=(
        ('1','Chef'),
        ('2','Waiter'),
        ('3','Busboy'),
        ('4','Cleaning staff'),
    )
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    date_of_birth=models.DateField()
    gender=models.CharField(max_length=1,choices=genders)
    duty_type=models.CharField(max_length=1,choices=duty_types)
    image = models.ImageField(null=True,blank=True)
    url = models.URLField(blank=True)
    restoran=models.ManyToManyField(Restourant)
    def __str__(self):
     return self.first_name

class About(models.Model):
    title=models.CharField(max_length=100)
    image = models.ImageField(null=True,blank=True)
    url = models.URLField(blank=True)
    description=models.TextField(validators=[MinLengthValidator(20)])
    description1=models.TextField(validators=[MinLengthValidator(20)])
    Restorant_id=models.ForeignKey(Restourant,on_delete=models.CASCADE,null=True)
    def __str__(self):
     return self.Restorant_id.name


class Specials(models.Model):
    name=models.CharField(max_length=100)
    image = models.ImageField(null=True,blank=True)
    url = models.URLField(blank=True)
    description=models.TextField(validators=[MinLengthValidator(20)])
    restoran=models.ForeignKey(Restourant,on_delete=models.CASCADE,null=True)
    def __str__(self):
     return self.name

class Contact(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=150)
    message=models.TextField(validators=[MinLengthValidator(10)])
    restoran=models.ForeignKey(Restourant,on_delete=models.CASCADE,null=True)
    def __str__(self):
     return self.name


class Adress(models.Model):
    province=models.CharField(max_length=100)
    district=models.CharField(max_length=100)
    quarter=models.CharField(max_length=100)
    person =models.OneToOneField(Person,on_delete=models.CASCADE,null=True)
    def __str__(self):
     return self.province
     
class Chef(models.Model):
    title=models.CharField(max_length=50)
    descripton=models.TextField(validators=[MinLengthValidator(10)])
    descripton1=models.TextField(validators=[MinLengthValidator(10)])
    image = models.ImageField(null=True,blank=True)
    url = models.URLField(blank=True)
    restoran=models.ForeignKey(Restourant,on_delete=models.CASCADE,null=True)


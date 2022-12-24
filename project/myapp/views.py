from django.shortcuts import render
from django.http import HttpResponse
from .models import About,Specials,Menu,Chef
# Create your views here.
def index(request):
    return render(request, 'index.html')
def specials(request):
    special=Specials.objects.all()
    return render(request, 'specials.html',{'special': special})
def about(request):
    abouts = About.objects.all()
    return render(request,'about.html',{'abouts': abouts})
def menu(request):
    menuss=Menu.objects.all()
    return render(request, 'menu.html',{'menuss': menuss})
def chef(request):
    chefs=Chef.objects.all()
    return render(request, 'chef.html',{'chefs': chefs})
def contact(request):
    return render(request, 'contact.html')
def rezervation(request):
    return render(request, 'rezervation.html')

 


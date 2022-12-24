"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from tkinter import Menu
from django.contrib import admin
from django.urls import path,include
from myapp import views as project
from django.conf.urls.static import static
from django.conf import settings
from myapp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', project.index,name='index'),
    path('specials/',project.specials,name='Specials'),
    path('about/',project.about,name='About'),
    path('menu/',project.menu,name='Menu'),
    path('chef/',project.chef,name='Chef'),
    path('contact/',project.contact,name='Contact'),
    path('rezervation/',project.rezervation,name='Rezervation'),
    path('accounts/', include('accounts.urls')),
    
]
urlpatterns += static(settings.MEDIA_URL, 
 document_root=settings.MEDIA_ROOT)
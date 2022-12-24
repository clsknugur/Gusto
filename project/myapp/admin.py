from django.contrib import admin
from .models import Restourant
from .models import Menu
from .models import Person
from .models import About
from .models import Specials
from .models import Contact
from .models import Adress
from .models import Chef

# Register your models here.
admin.site.register(Restourant)
admin.site.register(Menu)
admin.site.register(Person)
admin.site.register(About)
admin.site.register(Specials)
admin.site.register(Contact)
admin.site.register(Adress)
admin.site.register(Chef)



from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import userDat
from .models import Person
admin.site.register(userDat)
admin.site.register(Person)
#django
from django.contrib import admin
from django.urls import path, include

#local
from core import views

urlpatterns = [
    #list of path Api Object was refactoring to urls.py file in core folder
    path('', include ('core.urls'))
]

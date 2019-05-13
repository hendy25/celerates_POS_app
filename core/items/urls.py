#from
from django.urls import path, include

#rest
from rest_framework.routers import DefaultRouter

#local
from . import controllers

router = DefaultRouter()
router.register(r'', controllers.ItemController, basename='')

urlpatterns = [
    path('', include(router.urls))
]
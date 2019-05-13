#rest frame
from rest_framework.response import *
from rest_framework import status, views, viewsets, pagination, filters
from rest_framework import *
from datetime import datetime

#django
from django.contrib.contenttypes.models import *
from django.http import *

#3rd
from django_filters.rest_framework import DjangoFilterBackend

#local
from .serializers import *
from core.models import *
from core.utils import *

class ItemController(viewsets.ModelViewSet):
    serializer_class = ItemSerializer
    pagination_class = PagePagination
    queryset = Item.objects.all().filter(isDelete=False)
    filter_backend = [filters.SearchFilter, filters.OrderingFilter, DjangoFilterBackend]
    search_fields = ['itemId','itemName','itemDescription']
    filter_fields = ['itemPrice','itemQuantity','createdDate']

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.is_valid(raise_exception=True)
            #self.perform_create(serializer)

            itemName = serializer.data['itemName']
            itemDescription = serializer.data.get('itemDescription')
            itemPrice = serializer.data.get('itemPrice')
            itemQuantity = serializer.data.get('itemQantity')

            itemDescription += 'OK'

            items = Item.objects.create(
                itemName = itemName,
                itemDescription = itemDescription,
                itemPrice = itemPrice,
                itemQuantity = itemQuantity
            )
            items.save()

            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        else:
            return Response(serializer.error, status=status.HTTP_400_CREATED)
    
    def perform_destroy(self, instance):
        instance.idDelete=True
        instance.save()
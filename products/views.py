from rest_framework import generics
from rest_framework import permissions

from .models import Item
from .serializers import ItemSerializer


class ListCreateItems(generics.ListCreateAPIView):
    """
    List all available items
    Create new item
    """
    model = Item
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    permission_classes = [permissions.AllowAny, ]


class RetrieveUpdateDeleteItems(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update, delete an item by id
    """
    model = Item
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    permission_classes = [permissions.AllowAny, ]

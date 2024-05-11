from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .serializers import UserSerializer, MenuItemSerializer, BookingSerializer
from rest_framework import generics
from .models import *


# Create your views here.
def home(request):
    return render(request, 'index.html')


def links(request):
    return render(request, 'links.html')


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]


# ListCreateAPIView  = GET, POST
class MenuItemsView(generics.ListCreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer


# RetrieveUpdateDestroyAPIView = GET, PUT, PATCH, DELETE
class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer


class BookingViewSet(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]

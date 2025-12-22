from django.shortcuts import render
from rest_framework import viewsets
from django.contrib.auth.models import User
from .serializers import MenuSerializer, UserSerializer, BookingSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, DestroyAPIView
from .models import Menu, Booking
from rest_framework.viewsets import ModelViewSet
# Create your views here.
def index(request):
    return render(request, 'index.html', {})

class MenuItemView(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    
class SingleMenuItemView(RetrieveUpdateAPIView, DestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class BookingViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
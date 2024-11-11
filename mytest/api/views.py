from django.shortcuts import render 
from rest_framework import generics
from .serializers import MedicineSerializer, RefillSerializer, UserSerializer
from .models import Medicine, RefillRequest, User
from django.db.models import Count
# Create your views here.

class AddMedicineView(generics.CreateAPIView):
    queryset = Medicine.objects.all()
    serializer_class = MedicineSerializer

class ListMedicineView(generics.ListAPIView):
    queryset = Medicine.objects.all()
    serializer_class = MedicineSerializer


class AddRefillView(generics.CreateAPIView):
    queryset = RefillRequest.objects.all()
    serializer_class = RefillSerializer

class ListRefillView(generics.ListAPIView):
    queryset = RefillRequest.objects.values("medicine__name").annotate(
    total_requests = Count("id")
)
    serializer_class = RefillSerializer


class AddUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ListUserView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


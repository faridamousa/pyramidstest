from django.shortcuts import render 
from requests import Response
from rest_framework import generics
from .serializers import MedicineSerializer, RefillCountSerializer, RefillSerializer, UserSerializer
from .models import Medicine, RefillRequest, User
from django.db.models import Count
from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.views import APIView
from django.contrib.auth.models import User
# Create your views here.

class AddMedicineView(generics.CreateAPIView):
    queryset = Medicine.objects.all()
    serializer_class = MedicineSerializer
    permission_classes = [IsAuthenticated]

class ListMedicineView(generics.ListAPIView):
    queryset = Medicine.objects.all()
    serializer_class = MedicineSerializer
    permission_classes = [IsAuthenticated]


class AddRefillView(generics.CreateAPIView):
    queryset = RefillRequest.objects.all()
    serializer_class = RefillSerializer
    permission_classes = [IsAuthenticated]

class ListRefillView(generics.ListAPIView):
    queryset = RefillRequest.objects.values("medicine__name").annotate(refill_count=Count('id'))
    serializer_class = RefillCountSerializer
    permission_classes = [IsAuthenticated]
    
    
class AddUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

class ListUserView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    
class CreateUserView(generics.ListCreateAPIView):
    querySet = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]
from rest_framework import serializers
from .models import Medicine, RefillRequest, User

class MedicineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medicine
        fields = ('id', 'name', 'description', 
                  'dosage', 'available_quantity','created_at')


class RefillSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    medicine = serializers.StringRelatedField()
    class Meta:
        model = RefillRequest
        fields = ('id', 'user', 'medicine', 
                  'quantity','created_at')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'name', 'email', 
                  'password','created_at')
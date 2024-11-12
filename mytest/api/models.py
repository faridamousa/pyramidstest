from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class User (models.Model):
    username = models.CharField(max_length = 100)
    email = models. EmailField()
    password = models.CharField(max_length = 50)
    created_at = models.DateField(auto_now_add = True)

    def __str__(self):
        return f"{self.name}"

class Medicine (models.Model):
    name = models.CharField(max_length = 200)
    description = models.TextField()
    dosage = models.CharField(max_length = 50)
    available_quantity = models.IntegerField() 
    created_at = models.DateField(auto_now_add = True)

    def __str__(self):
        return f"{self.name}"

class RefillRequest (models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    medicine = models.ForeignKey(Medicine, on_delete = models.CASCADE)
    created_at = models.DateField(auto_now_add = True)


    def __str__(self):
        return f"refill request for {self.medicine.name} by {self.user.name} "



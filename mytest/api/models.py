from django.db import models

# Create your models here.

class User (models.Model):
    first_name = models.CharField(max_length = 100)
    last_name = models.CharField(max_length = 100)
    email = models. EmailField()
    username = models.CharField(max_length = 50)
    password = models.CharField(max_length = 50)
    created_at = models.DateField(auto_now_add = True)

    def __str__(self):
        return f"User created {self.first_name} {self.last_name}"

class Medicine (models.Model):
    name = models.CharField(max_length = 200)
    description = models.TextField()
    dosage = models.CharField(max_length = 50)
    available_quantity = models.IntegerField() 
    created_at = models.DateField(auto_now_add = True)

    def __str__(self):
        return f"Medicine name {self.name}"

class RefillRequest (models.Model):
    user = models.ForeignKey("User", on_delete = models.CASCADE)
    medicine = models.ForeignKey("Medicine", on_delete = models.CASCADE)
    quantity = models.IntegerField()
    status = models.CharField(max_length = 30, choices =[ ('pending', 'Pending'), ('approved', 'Approved'), ['rejected','Rejected']] )
    created_at = models.DateField(auto_now_add = True)


    def __str__(self):
        return f"refill request for {self.medicine.name} by {self.user.first_name} {self.user.last_name}"
    
def count():
    return RefillRequest.objects.count()


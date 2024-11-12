from django.contrib import admin

from .models import Medicine, RefillRequest, User

# Register your models here.

admin.site.register(User)
admin.site.register(Medicine)
admin.site.register(RefillRequest)
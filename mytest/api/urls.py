from django.urls import path, include
from .views import AddMedicineView, ListMedicineView, AddRefillView, ListRefillView, AddUserView, ListUserView
urlpatterns = [
    path('addMedicine', AddMedicineView.as_view()),
    path('listMedicine', ListMedicineView.as_view()),

    path('addRefill', AddRefillView.as_view()),
    path('listRefill', ListRefillView.as_view()),

    path('addUser', AddUserView.as_view()),
    path('listUser', ListUserView.as_view()),

]
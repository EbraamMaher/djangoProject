from django.urls import path
from Cars.views import CarsIndex, CarDetails, CreateCarView, EditCarView, DeleteCarView


urlpatterns = [
    path('index', CarsIndex),
    path('<int:pk>', CarDetails.as_view(), name='Cars.show'),
    path('create', CreateCarView.as_view(),name='Cars.create'),
    path('edit/<int:pk>', EditCarView.as_view(), name='Cars.edit'),
    path('delete/<int:pk>', DeleteCarView.as_view(), name='Cars.delete'),
]

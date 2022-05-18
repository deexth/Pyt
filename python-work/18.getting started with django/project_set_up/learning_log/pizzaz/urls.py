from django.urls import path
from . import views


app_name = 'pizzaz'

# Urls goes here
urlpatterns = [
    path('', views.index, name='pizza_index'),
    path('delice/<int:pizzaz_id>', views.toppings, name='toppings'),
]

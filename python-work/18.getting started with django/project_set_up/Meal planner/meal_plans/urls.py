from django.urls import path
from . import views


# urls here
app_name = 'meal_plans'

# home page
urlpatterns = [
    path("", views.index, name="index"),
]


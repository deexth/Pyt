# Define url patterns for users.
from django.urls import path, include
from . import views


app_name = 'users'
urlpatterns = [
    # Include default urls
    path('', include('django.contrib.auth.urls')),
    path('register/', views.register, name="register"),
]

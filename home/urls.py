from django.contrib import admin
from django.urls import path
from home import views

# HTTP Request <-> HTTP Reponse
# MVT (MVC)

urlpatterns = [
    path('', views.home), 
]

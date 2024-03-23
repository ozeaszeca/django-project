from django.contrib import admin
from django.urls import path
from blog import views

# HTTP Request <-> HTTP Reponse
# MVT (MVC)

urlpatterns = [
    path('', views.blog),
    path('exemplo/', views.exemplo)
]

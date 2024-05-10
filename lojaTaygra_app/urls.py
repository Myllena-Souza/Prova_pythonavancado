from django.urls import path
from lojaTaygra_app import views

urlpatterns = [
    path('', views.home, name= 'home'),
]

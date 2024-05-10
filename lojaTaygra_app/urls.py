from django.urls import path
from lojaTaygra_app import views

urlpatterns = [
    path('', views.home, name= 'home'),
    path('sobre/', views.sobre, name= 'sobre'),
    path('contato/', views.contato, name= 'contato'),
    path('promocao/', views.promocao, name= 'promocao'),
    path('add_produtos/', views.add_produtos, name = 'add_produtos'),
    path('login/',  views.login, name = 'login'),
    path('logout/',  views.logout, name = 'logout'),
    path('cadastrouser/',  views.cadastrouser, name = 'cadastrouser'),
]

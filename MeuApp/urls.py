from django.urls import path 
from MeuApp import views

#registrar as Urlsdo App

#Qual url corresponde a cada view
urlpatterns =[
    path('', views.home, name='name'),
    path('contato/', views.contato, name='contato'),
    path('produto/', views.exibir_produtos, name='produtos')
]
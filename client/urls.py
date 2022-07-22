import imp
from django.urls import path
from . import views

urlpatterns=[
    path('',views.clients, name="clients"),
    path('<slug:category_slug>/', views.clients, name="clients_by_category"),
    path('<int:id>/<slug:slug>/', views.client_detail, name="client_detail"),
]
from django.urls import path
from . import views

urlpatterns = [
    path('',views.wedding, name="wedding"),
    path('<slug:category_slug>/', views.wedding, name="wedding_by_category"),
]
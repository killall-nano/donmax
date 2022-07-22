from . import views
from django.urls import path

urlpatterns = [
    path('',views.index, name="index"),
    path('investments/',views.investments, name="investments"),
    path('about-me/',views.about, name="about-me"),
    path('contact/',views.contact, name="contact"),
]
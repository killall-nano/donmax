from django.urls import path
from . import views

urlpatterns = [
    path('',views.portfolio, name="portfolio"),
    path('<slug:category_slug>/', views.portfolio, name="portfolio_by_category"),
]
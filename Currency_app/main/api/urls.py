from django.urls import path
from main.api import views

urlpatterns = [
    path('', views.currency_list),
    path('<int:pk>/', views.currency_detail),
]
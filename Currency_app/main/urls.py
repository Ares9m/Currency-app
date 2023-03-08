from django.urls import path

from . import views
# from .views import CurrencyList, CurrencyDetail
# . => from current directory

urlpatterns = [
    path("", views.index, name="index"),
    path("home/", views.index, name="index"),
    path("login/", views.login_page, name="login"),
]
from django.shortcuts import render
from django.http import HttpResponse
# from django.core import serializers
from .models import Currency

# Create your views (webpages) here.

def index(response):
    curr = Currency.objects.all()
    return render(response, "main/home.html", {"curr":curr})

def login_page(response):
    return HttpResponse("<h1>this is going to be a login page</h1>")

# fetching currency and saving in python dictionary
# curr = serializers.serialize("python", Currency.objects.all())
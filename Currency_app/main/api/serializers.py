from rest_framework import serializers
from main.models import Currency

# serializers package data coming from you into the server 
# and unpackage data coming from the server

class CurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Currency
        fields = ["id", "name", "symbol", "exchange_rate"]
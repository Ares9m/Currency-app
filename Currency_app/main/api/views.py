from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from main.models import Currency
from main.api.serializers import CurrencySerializer

"""
request.POST  # Only handles form data.  Only works for 'POST' method.
request.data  # Handles arbitrary data.  Works for 'POST', 'PUT' and 'PATCH' methods.

return Response(data)  # Renders to content type as requested by the client.
"""

# handles adding and listing
# gets every currecy
# serializes them
# returns json
@api_view(['GET', 'POST'])
def currency_list(request):
    """
    List all code currency, or create a new currency.
    """
    if request.method == 'GET':
        currency = Currency.objects.all()
        serializer = CurrencySerializer(currency, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = CurrencySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def currency_detail(request, pk):
    """
    Retrieve, update or delete a code currency.
    """
    try:
        currency = Currency.objects.get(pk=pk)
    except Currency.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CurrencySerializer(currency)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = CurrencySerializer(currency, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        currency.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

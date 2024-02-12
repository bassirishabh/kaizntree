import logging
import requests
from django.shortcuts import render
from rest_framework import generics
from .models import Item, ProductionOrder
from .serializers import ItemSerializer
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User


logger = logging.getLogger(__name__)

class ItemListView(generics.ListAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

    user = User.objects.get(username='rishabhbassi')
    token, created = Token.objects.get_or_create(user=user)
    print(token.key)

    token = token.key
    headers = {'Authorization': f'Token {token}'}

    def get_queryset(self):
        try:
            response = requests.get('http://127.0.0.1:8000/api/api/items/', headers=self.headers)
            response.raise_for_status()  # Raise exception for non-2xx responses
            return Item.objects.all()  # Return queryset based on response data
        except requests.RequestException as e:
            logger.error(f"Request failed: {e}")
            return Item.objects.none()  # Return empty queryset or handle error accordingly

def item_dashboard(request):
    items = Item.objects.all()
    return render(request, 'item_dashboard.html', {'items': items})

def build_dashboard(request):
    production_orders = ProductionOrder.objects.all()
    return render(request, 'build_dashboard.html', {'production_orders': production_orders})

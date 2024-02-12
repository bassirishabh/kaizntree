from rest_framework.test import APITestCase
from rest_framework import status
from .models import Item

class ItemAPITestCase(APITestCase):
    def setUp(self):
        self.item = Item.objects.create(
            sku='12345',
            name='Test Item',
        )

    def test_get_item_list(self):
        response = self.client.get('/api/items/')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.client.credentials(HTTP_AUTHORIZATION='Token 5026e4bad347c6d6e31a6c971cb0e0cfd2a565a0')
        response = self.client.get('/api/items/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

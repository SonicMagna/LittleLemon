from django.test import TestCase
from restaurant.models import MenuItem

from rest_framework.test import APIClient
from .serializers import MenuItemSerializer


class MenuItemTest(TestCase):
  def test_get_item(self):
    item = MenuItem.objects.create(title="IceCream", price=2.55, inventory=1)
    self.assertEqual(str(item), "IceCream : 2.55")


class MenuItemsView(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.menu_item1 = MenuItem.objects.create(title="Burger", price=10.99, inventory=50)
        self.menu_item2 = MenuItem.objects.create(title="Pizza", price=12.99, inventory=40)

    def test_getall(self):
        response = self.client.get('/api/menu-items')
        menu_items = MenuItem.objects.all()
        serializer = MenuItemSerializer(menu_items, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, 200)
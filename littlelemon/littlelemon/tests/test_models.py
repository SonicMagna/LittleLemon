from django.test import TestCase
from .models import MenuItem

class MenuItemTest(TestCase):
  def test_get_item(self):
    item = MenuItem.objects.create(title="IceCream", price=2.55, inventory=1)
    self.assertEqual(str(item), "IceCream : 2.55")
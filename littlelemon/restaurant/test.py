from django.test import TestCase
from restaurant.models import MenuItem

# Create your tests here.
class MenuItemTest(TestCase):
  def test_get_item(self):
    item = MenuItem.objects.create(title="IceCream", price=2.55, inventory=1)
    self.assertEqual(item, "IceCream : 2.55")

# I never could get this thing to pass. I don't know why it doesn't work...
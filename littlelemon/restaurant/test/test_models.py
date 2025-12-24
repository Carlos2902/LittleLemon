from django.test import TestCase
from ..models import Menu

# [{"id":1,"Title":"CHICKEN WINGS","Price":"10.00","Inventory":2}]%

class MenuItemTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(Title="CHICKEN WINGS", Price=10.00, Inventory=2)
        itemstr = item.get_item()
        self.assertEqual(itemstr, "CHICKEN WINGS: 10.00")
        

from django.test import TestCase
from ..models import Menu
from rest_framework.test import APIClient
from ..serializers import MenuSerializer

from django.contrib.auth.models import User

class MenuViewTest(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass'
        )
        self.client.force_authenticate(user=self.user)

        Menu.objects.create(Title="CHICKEN WINGS", Price=10.00, Inventory=2)
        Menu.objects.create(Title="FRENCH FRIES", Price=5.00, Inventory=5)

    def test_getall(self):
        response = self.client.get('/restaurant/menu/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 2)

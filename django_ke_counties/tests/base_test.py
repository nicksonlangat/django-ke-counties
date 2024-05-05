from django.test import TransactionTestCase
from rest_framework.test import APIClient


class BaseTest(TransactionTestCase):
    def setUp(self):
        self.client = APIClient()

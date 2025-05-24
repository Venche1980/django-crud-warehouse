from django.test import TestCase
from logistic.models import Product, Stock

class ModelTests(TestCase):
    def test_product_creation(self):
        """Проверяем, что товар создаётся корректно"""
        product = Product.objects.create(name="Тестовый товар", description="Описание")
        self.assertEqual(product.name, "Тестовый товар")

    def test_stock_creation(self):
        """Проверяем, что остаток на складе создаётся корректно"""
        stock = Stock.objects.create(address="Тестовый адрес")
        self.assertEqual(stock.address, "Тестовый адрес")

from django.test import TestCase
from logistic.models import Product, Stock, StockProduct


class ModelTests(TestCase):
    def test_product_creation(self):
        """Проверяем, что товар создаётся корректно"""
        product = Product.objects.create(title="Тестовый товар", description="Описание")
        self.assertEqual(product.title, "Тестовый товар")

    def test_stock_creation(self):
        """Проверяем, что склад создаётся корректно"""
        stock = Stock.objects.create(address="Тестовый адрес")
        self.assertEqual(stock.address, "Тестовый адрес")

    def test_stockproduct_creation(self):
        """Проверяем, что связь StockProduct создаётся корректно"""
        product = Product.objects.create(title="Тестовый товар")
        stock = Stock.objects.create(address="Тестовый адрес")
        position = StockProduct.objects.create(stock=stock, product=product, quantity=10, price=100)
        self.assertEqual(position.quantity, 10)
        self.assertEqual(position.price, 100)
        self.assertEqual(position.product.title, "Тестовый товар")
        self.assertEqual(position.stock.address, "Тестовый адрес")

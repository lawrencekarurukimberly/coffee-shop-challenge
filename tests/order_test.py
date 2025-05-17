import unittest
from customer import Customer
from coffee import Coffee
from order import Order

class TestOrder(unittest.TestCase):
    def setUp(self):
        self.customer = Customer("Alice")
        self.coffee = Coffee("Latte")
        self.order = Order(self.customer, self.coffee, 5.0)

    def test_price_validation(self):
        with self.assertRaises(ValueError):
            Order(self.customer, self.coffee, 0.5)  # Too low
        with self.assertRaises(ValueError):
            Order(self.customer, self.coffee, 11.0)  # Too high
        with self.assertRaises(ValueError):
            Order(self.customer, self.coffee, "5")  # Wrong type

    def test_customer_validation(self):
        with self.assertRaises(ValueError):
            Order("Not a customer", self.coffee, 5.0)

    def test_coffee_validation(self):
        with self.assertRaises(ValueError):
            Order(self.customer, "Not a coffee", 5.0)

    def test_price_immutable(self):
        with self.assertRaises(AttributeError):
            self.order.price = 6.0

    def test_customer_property(self):
        self.assertEqual(self.order.customer, self.customer)

    def test_coffee_property(self):
        self.assertEqual(self.order.coffee, self.coffee)

if __name__ == '__main__':
    unittest.main()
import unittest
from customer import Customer
from coffee import Coffee
from order import Order

class TestCoffee(unittest.TestCase):
    def setUp(self):
        self.coffee = Coffee("Latte")
        self.customer = Customer("Alice")
        self.order = Order(self.customer, self.coffee, 5.0)

    def test_name_validation(self):
        with self.assertRaises(ValueError):
            Coffee("Ab")  # Too short
        with self.assertRaises(ValueError):
            Coffee(123)  # Wrong type

    def test_name_immutable(self):
        with self.assertRaises(AttributeError):
            self.coffee.name = "Mocha"

    def test_orders(self):
        self.assertEqual(self.coffee.orders(), [self.order])

    def test_customers(self):
        self.assertEqual(self.coffee.customers(), [self.customer])

    def test_num_orders(self):
        self.assertEqual(self.coffee.num_orders(), 1)

    def test_average_price(self):
        Order(self.customer, self.coffee, 7.0)
        self.assertEqual(self.coffee.average_price(), 6.0)

if __name__ == '__main__':
    unittest.main()
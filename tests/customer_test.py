import unittest
from customer import Customer
from coffee import Coffee
from order import Order

class TestCustomer(unittest.TestCase):
    def setUp(self):
        self.customer = Customer("Alice")
        self.coffee = Coffee("Latte")
        self.order = Order(self.customer, self.coffee, 5.0)

    def test_name_validation(self):
        with self.assertRaises(ValueError):
            Customer("")  # Too short
        with self.assertRaises(ValueError):
            Customer("A" * 16)  # Too long
        with self.assertRaises(ValueError):
            Customer(123)  # Wrong type

    def test_name_setter(self):
        self.customer.name = "Bob"
        self.assertEqual(self.customer.name, "Bob")
        with self.assertRaises(ValueError):
            self.customer.name = "A" * 16

    def test_orders(self):
        self.assertEqual(self.customer.orders(), [self.order])

    def test_coffees(self):
        self.assertEqual(self.customer.coffees(), [self.coffee])

    def test_create_order(self):
        new_coffee = Coffee("Espresso")
        order = self.customer.create_order(new_coffee, 3.0)
        self.assertEqual(order.customer, self.customer)
        self.assertEqual(order.coffee, new_coffee)
        self.assertEqual(order.price, 3.0)

    def test_most_aficionado(self):
        customer2 = Customer("Bob")
        Order(customer2, self.coffee, 7.0)
        self.assertEqual(Customer.most_aficionado(self.coffee), customer2)

if __name__ == '__main__':
    unittest.main()
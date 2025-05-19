import pytest
from order import Order
from customer import Customer
from coffee import Coffee

def test_order_valid_init():
    customer = Customer("Alice")
    coffee = Coffee("Latte")
    order = Order(customer, coffee, 5.0)
    assert order.customer == customer
    assert order.coffee == coffee
    assert order.price == 5.0

def test_order_invalid_price_range():
    customer = Customer("Alice")
    coffee = Coffee("Latte")
    with pytest.raises(ValueError):
        Order(customer, coffee, 11.0)
    with pytest.raises(ValueError):
        Order(customer, coffee, 0.5)

def test_order_invalid_price_type():
    customer = Customer("Alice")
    coffee = Coffee("Latte")
    with pytest.raises(ValueError):
        Order(customer, coffee, "5.0")

def test_order_invalid_customer_coffee():
    coffee = Coffee("Espresso")
    customer = Customer("Bob")
    with pytest.raises(ValueError):
        Order("NotACustomer", coffee, 5.0)
    with pytest.raises(ValueError):
        Order(customer, "NotACoffee", 5.0)

def test_order_price_immutable():
    customer = Customer("Bob")
    coffee = Coffee("Espresso")
    order = Order(customer, coffee, 4.0)
    with pytest.raises(AttributeError):
        order.price = 6.0
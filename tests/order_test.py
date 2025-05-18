import pytest
from order import Order
from customer import Customer
from coffee import Coffee


def test_order_init():
    customer = Customer("Alice")
    coffee = Coffee("Latte")
    order = Order(customer, coffee, 5.0)
    assert order.customer == customer
    assert order.coffee == coffee
    assert order.price == 5.0
    with pytest.raises(ValueError):
        Order(customer, coffee, 11.0)
    with pytest.raises(ValueError):
        Order(customer, coffee, "5.0")
    with pytest.raises(ValueError):
        Order("Not a customer", coffee, 5.0)
    with pytest.raises(ValueError):
        Order(customer, "Not a coffee", 5.0)


def test_price_immutable():
    customer = Customer("Bob")
    coffee = Coffee("Espresso")
    order = Order(customer, coffee, 4.0)
    with pytest.raises(AttributeError):
        order.price = 5.0
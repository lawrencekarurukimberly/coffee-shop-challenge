import pytest
from customer import Customer
from coffee import Coffee
from order import Order


def test_customer_name():
    customer = Customer("Alice")
    assert customer.name == "Alice"
    with pytest.raises(ValueError):
        customer.name = ""
    with pytest.raises(ValueError):
        customer.name = "A" * 16
    with pytest.raises(ValueError):
        customer.name = 123


def test_customer_orders():
    customer = Customer("Bob")
    coffee = Coffee("Latte")
    order = Order(customer, coffee, 4.5)
    assert customer.orders() == [order]


def test_customer_coffees():
    customer = Customer("Charlie")
    coffee1 = Coffee("Mocha")
    coffee2 = Coffee("Espresso")
    Order(customer, coffee1, 5.0)
    Order(customer, coffee2, 3.5)
    assert set(customer.coffees()) == {coffee1, coffee2}


def test_create_order():
    customer = Customer("Dave")
    coffee = Coffee("Cappuccino")
    order = customer.create_order(coffee, 6.0)
    assert order in customer.orders()
    assert order.coffee == coffee


def test_most_aficionado():
    coffee = Coffee("Americano")
    customer1 = Customer("Eve")
    customer2 = Customer("Frank")
    Order(customer1, coffee, 5.0)
    Order(customer1, coffee, 5.0)
    Order(customer2, coffee, 3.0)
    assert Customer.most_aficionado(coffee) == customer1
    assert Customer.most_aficionado(Coffee("Empty")) is None
import pytest
from coffee import Coffee
from customer import Customer
from order import Order

def test_coffee_name_valid():
    coffee = Coffee("Latte")
    assert coffee.name == "Latte"

def test_coffee_name_immutable():
    coffee = Coffee("Latte")
    with pytest.raises(AttributeError):
        coffee.name = "Mocha"

def test_coffee_name_invalid():
    with pytest.raises(ValueError):
        Coffee("Ab") 
    with pytest.raises(ValueError):
        Coffee(123)   

def test_coffee_orders():
    coffee = Coffee("Espresso")
    customer = Customer("Alice")
    order = Order(customer, coffee, 4.0)
    assert coffee.orders() == [order]

def test_coffee_customers():
    coffee = Coffee("Mocha")
    customer1 = Customer("Bob")
    customer2 = Customer("Charlie")
    Order(customer1, coffee, 5.0)
    Order(customer2, coffee, 3.5)
    assert set(coffee.customers()) == {customer1, customer2}

def test_num_orders():
    coffee = Coffee("Cappuccino")
    customer = Customer("Dave")
    Order(customer, coffee, 6.0)
    Order(customer, coffee, 4.5)
    assert coffee.num_orders() == 2

def test_average_price():
    coffee = Coffee("Americano")
    customer = Customer("Eve")
    Order(customer, coffee, 5.0)
    Order(customer, coffee, 3.0)
    assert coffee.average_price() == 4.0

def test_average_price_empty():
    assert Coffee("Empty").average_price() == 0
from customer import Customer
from coffee import Coffee
from order import Order

if __name__ == "__main__":
    customer1 = Customer("Alice")
    customer2 = Customer("Bob")
    coffee1 = Coffee("Espresso")
    coffee2 = Coffee("Latte")
    order1 = Order(customer1, coffee1, 5.0)
    order2 = Order(customer1, coffee2, 3.5)
    order3 = Order(customer2, coffee1, 4.0)

    print(customer1.coffees())
    print(coffee1.customers())
    print(coffee1.num_orders())
    print(coffee1.average_price())
    print(Customer.most_aficionado(coffee1))
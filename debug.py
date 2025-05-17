from customer import Customer
from coffee import Coffee
from order import Order

def debug():
    # Create some test data
    customer1 = Customer("Alice")
    customer2 = Customer("Bob")
    coffee1 = Coffee("Latte")
    coffee2 = Coffee("Espresso")

    order1 = Order(customer1, coffee1, 5.0)
    order2 = Order(customer1, coffee2, 3.0)
    order3 = Order(customer2, coffee1, 7.0)

    # Test relationships
    print(f"Customer1 orders: {len(customer1.orders())}")  # Should be 2
    print(f"Customer1 coffees: {[coffee.name for coffee in customer1.coffees()]}")  # Latte, Espresso
    print(f"Coffee1 orders: {coffee1.num_orders()}")  # Should be 2
    print(f"Coffee1 average price: {coffee1.average_price()}")  # Should be 6.0
    print(f"Most aficionado for Latte: {Customer.most_aficionado(coffee1).name}")  # Should be Bob

if __name__ == "__main__":
    debug()
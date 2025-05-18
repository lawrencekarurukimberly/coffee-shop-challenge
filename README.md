# Coffee Shop Code Challenge

This is a Python project implementing a Coffee Shop domain with object relationships between `Customer`, `Coffee`, and `Order` classes.

---

## Project Overview

The goal of this challenge is to model a coffee shop system that manages customers, coffee products, and orders with the following relationships:

- A **Customer** can place many **Orders**.
- A **Coffee** product can have many **Orders**.
- An **Order** belongs to one **Customer** and one **Coffee**.
- Thus, **Coffee** and **Customer** share a many-to-many relationship via **Orders**.

---

## Features

- Proper initialization and validation of attributes for each model.
- Object relationship methods that allow querying orders, coffees, and customers.
- Aggregate methods to calculate stats like number of orders and average price.
- Bonus feature: Identify the customer who spent the most on a specific coffee.

---

## Project Structure

coffee-shop-challenge/
├── Pipfile
├── customer.py
├── coffee.py
├── order.py
├── debug.py
└── tests/
├── customer_test.py
├── coffee_test.py
└── order_test.py


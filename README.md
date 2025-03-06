# module2Lesson6

## Python Object-Oriented Programming (OOP) Exercises

This project covers the fundamentals of Object-Oriented Programming (OOP) in Python. The main focus is on understanding key OOP concepts such as classes, objects, inheritance, polymorphism, and encapsulation. The provided exercises demonstrate how to apply these principles through practical Python examples.

## Exercises Overview

1. **Mid-Lesson Exercise: Create a Car Class**
   - **Task:** Create a class representing a Car with attributes such as `make`, `model`, and `mileage`. Implement methods for displaying car information.
   - **Solution:** The script defines a `Car` class, instantiates a car object, and demonstrates how to use methods to access and modify its attributes.

2. **Final Exercise: Bank Account Class**
   - **Task:** Write a Python class that simulates a bank account. Implement methods for depositing and withdrawing money, and checking account balance.
   - **Solution:** The `BankAccount` class is defined with methods for depositing, withdrawing, and checking balance. The script creates an account object and performs these operations.

## Code

### 1. Mid-Lesson Exercise: Create a Car Class

```python
class Car:
    def __init__(self, make, model, mileage=0):
        self.make = make
        self.model = model
        self.mileage = mileage

    def display_info(self):
        return f"{self.make} {self.model}, Mileage: {self.mileage} miles"

# Creating an object (instance) of the class
my_car = Car("Toyota", "Corolla", 10000)
print(my_car.display_info())  # Output: Toyota Corolla, Mileage: 10000 miles

# Lesson 6: Object-Oriented Programming Fundamentals - Engage & Apply + Final Challenge

# ===========================
# engage and apply ---------> Exercise 1 pre-provided
# ===========================

# Task: Create a Car class with attributes like make, model, and mileage.
# Also, define methods to display car information and update mileage after a drive.

# Solution:
class Car:
    def __init__(self, make, model, mileage=0):
        # Instance attributes
        self.make = make
        self.model = model
        self.mileage = mileage

    # Method to display car information
    def display_info(self):
        return f"{self.make} {self.model}, Mileage: {self.mileage} miles"

    # Method to update mileage
    def drive(self, miles):
        self.mileage += miles
        return f"Drove {miles} miles. Total mileage is now {self.mileage} miles."

# Creating an instance of the Car class
my_car = Car("Toyota", "Corolla", 10000)

# Using the methods
print(my_car.display_info())  # Output: Toyota Corolla, Mileage: 10000 miles
print(my_car.drive(150))      # Output: Drove 150 miles. Total mileage is now 10150 miles

# ===========================
# engage and apply ---------> Exercise 1 My Version Created
# ===========================

# Task: Create a Person class with instance attributes name and age.
# Include methods like greet() and have_birthday() to interact with the attributes.

# Solution:
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Method to greet the person
    def greet(self):
        return f"Hello, my name is {self.name}!"

    # Method to simulate a birthday
    def have_birthday(self):
        self.age += 1
        return f"Happy Birthday! You are now {self.age} years old."

# Creating an instance of Person
person1 = Person("Alice", 25)

# Using the methods
print(person1.greet())            # Output: Hello, my name is Alice!
print(person1.have_birthday())    # Output: Happy Birthday! You are now 26 years old.

# ===========================
# final challenge ---------> pre-provided
# ===========================

# Task: Create a BankAccount class with attributes like account_holder and balance.
# Methods should include deposit, withdraw, and get_balance.

# Solution:
class BankAccount:
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.balance = balance

    # Method to deposit money
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return f"Deposited ${amount}. New balance: ${self.balance}"
        else:
            return "Deposit amount must be positive."

    # Method to withdraw money
    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            return f"Withdrew ${amount}. New balance: ${self.balance}"
        else:
            return "Insufficient funds or invalid amount."

    # Method to check the balance
    def get_balance(self):
        return f"Current balance: ${self.balance}"

# Creating an instance of BankAccount
account = BankAccount("Alice", 100)

# Testing the methods
print(account.get_balance())    # Output: Current balance: $100.00
print(account.deposit(50))      # Output: Deposited $50.00. New balance: $150.00
print(account.withdraw(30))     # Output: Withdrew $30.00. New balance: $120.00
print(account.withdraw(200))    # Output: Insufficient funds or invalid amount.

# ===========================
# final challenge ---------> My Version Created
# ===========================

# Task: Write a script to create a Person class with instance attributes name and age.
# Add methods greet() and have_birthday() to interact with those attributes.

# Solution:
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Method to greet the person
    def greet(self):
        return f"Hi! I'm {self.name}, nice to meet you!"

    # Method to simulate a birthday
    def have_birthday(self):
        self.age += 1
        return f"Cheers! You're now {self.age} years old!"

# Creating an instance of Person
person2 = Person("Bob", 30)

# Using the methods
print(person2.greet())            # Output: Hi! I'm Bob, nice to meet you!
print(person2.have_birthday())    # Output: Cheers! You're now 31 years old!


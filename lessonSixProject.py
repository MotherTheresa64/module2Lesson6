# Lesson 6: Object Oriented Programming - Engage & Apply + Final Challenge

# ===========================
# engage and apply ---------> Exercise 1 pre-provided
# ===========================

# Task: Create a class named `Person` with instance attributes name (string) and age (integer).
# Add two instance methods:
# - greet(): This method should return a greeting message that includes the person's name.
# - have_birthday(): This method should increase the person's age by one and return a message that says,
# "Happy Birthday! You are now [age] years old."

class Person:
    def __init__(self, name, age):
        # Instance Attributes
        self.name = name
        self.age = age

    # Method to greet the person
    def greet(self):
        return f"Hello, my name is {self.name}!"

    # Method to simulate a birthday
    def have_birthday(self):
        self.age += 1
        return f"Happy Birthday! You are now {self.age} years old."

# Creating an instance of the Person class
person1 = Person("Alice", 25)

# Using the methods
print(person1.greet())            # Output: Hello, my name is Alice!
print(person1.have_birthday())    # Output: Happy Birthday! You are now 26 years old.

# ===========================
# engage and apply ---------> Exercise 1 My Version Created
# ===========================

# Task: Create a `Person` class with name (string) and age (integer) attributes, and include two methods: greet() and have_birthday().
# Write a script to interact with the `Person` class.

# Sample Usage
person2 = Person("Bob", 30)

# Testing the methods
print(person2.greet())            # Output: Hello, my name is Bob!
print(person2.have_birthday())    # Output: Happy Birthday! You are now 31 years old.

# ===========================
# final challenge ---------> pre-provided
# ===========================

# Task: Create a BankAccount class with instance attributes:
# - account_holder (string): The name of the account holder.
# - balance (float): The current account balance, defaulting to 0.
# Methods:
# - deposit(amount): Adds the given amount to the account balance and returns a message showing the new balance.
# - withdraw(amount): Subtracts the given amount from the balance if there are sufficient funds. Otherwise, it should return a message saying "Insufficient funds." If the withdrawal is successful, it should return the new balance.
# - get_balance(): Returns a message displaying the current account balance.

class BankAccount:
    def __init__(self, account_holder, balance=0):
        # Instance Attributes
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

# Task: Create a BankAccount class with attributes account_holder and balance, along with methods to deposit, withdraw, and check balance.

# Sample Usage
account2 = BankAccount("Bob", 500)

# Testing the methods
print(account2.get_balance())    # Output: Current balance: $500.00
print(account2.deposit(100))     # Output: Deposited $100.00. New balance: $600.00
print(account2.withdraw(150))    # Output: Withdrew $150.00. New balance: $450.00
print(account2.withdraw(500))    # Output: Insufficient funds or invalid amount.

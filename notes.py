# Lesson 6: Object Oriented Programming - Notes and Key Takeaways

# ===========================
# engage and apply ---------> Key Concept: Object-Oriented Programming (OOP)
# ===========================

# OOP is a programming paradigm based on the concept of objects, which are instances of classes.
# Key OOP Concepts:
# 1. Class: A blueprint for creating objects (instances).
# 2. Object: An instance of a class.
# 3. Methods: Functions defined within a class that operate on the object.
# 4. Attributes: Variables that hold data specific to an object.
# 5. Inheritance: A mechanism to create a new class based on an existing class.
# 6. Encapsulation: Bundling the data and methods that operate on the data within one unit.
# 7. Polymorphism: The ability to use the same method name but have it behave differently based on the object.

# Example of Class and Object in Python
class Dog:
    def __init__(self, name, age):
        # Instance Attributes
        self.name = name
        self.age = age

    def speak(self):
        return f"{self.name} says Woof!"

# Creating an object (instance) of the Dog class
dog1 = Dog("Rex", 4)
print(dog1.speak())  # Output: Rex says Woof!

# ===========================
# engage and apply ---------> Class, Methods, and Attributes in Practice
# ===========================

# To create a class in Python, use the "class" keyword. Define methods with "def" and include the self parameter to refer to the instance.
# Example of adding a method that modifies an object's state.

class Person:
    def __init__(self, name, age):
        # Instance Attributes
        self.name = name
        self.age = age

    def greet(self):
        return f"Hello, my name is {self.name}!"

    def have_birthday(self):
        self.age += 1
        return f"Happy Birthday! You are now {self.age} years old."

# Creating an object and interacting with its methods
person1 = Person("Alice", 25)
print(person1.greet())  # Output: Hello, my name is Alice!
print(person1.have_birthday())  # Output: Happy Birthday! You are now 26 years old.

# ===========================
# final challenge ---------> Using OOP for Practical Applications
# ===========================

# Task: Create a BankAccount class to simulate a bank account with deposit and withdrawal functionality.
# The BankAccount class includes the following methods:
# - __init__: Initializes the account holder name and balance.
# - deposit: Adds funds to the account.
# - withdraw: Subtracts funds from the account, ensuring sufficient funds are available.
# - get_balance: Returns the current balance of the account.

class BankAccount:
    def __init__(self, account_holder, balance=0):
        # Instance Attributes
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return f"Deposited ${amount}. New balance: ${self.balance}"
        else:
            return "Deposit amount must be positive."

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            return f"Withdrew ${amount}. New balance: ${self.balance}"
        else:
            return "Insufficient funds or invalid amount."

    def get_balance(self):
        return f"Current balance: ${self.balance}"

# Example Usage of BankAccount class
account = BankAccount("Alice", 100)
print(account.get_balance())  # Output: Current balance: $100
print(account.deposit(50))  # Output: Deposited $50. New balance: $150
print(account.withdraw(30))  # Output: Withdrew $30. New balance: $120

# ===========================
# final challenge ---------> Notes on Inheritance and Extending Functionality
# ===========================

# Inheritance allows us to create a new class that reuses the methods and attributes of an existing class.
# This is useful when we want to extend the functionality of an existing class or create more specialized objects.

class SavingsAccount(BankAccount):
    def __init__(self, account_holder, balance=0, interest_rate=0.05):
        # Call to the parent class's __init__ method
        super().__init__(account_holder, balance)
        # Additional attribute for interest rate
        self.interest_rate = interest_rate

    # Method to calculate interest
    def add_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        return f"Interest added. New balance: ${self.balance}"

# Example usage of SavingsAccount class (which inherits from BankAccount)
savings_account = SavingsAccount("Bob", 500)
print(savings_account.get_balance())  # Output: Current balance: $500
print(savings_account.add_interest())  # Output: Interest added. New balance: $525.0

# ===========================
# final challenge ---------> My Version Created
# ===========================

# Task: Extend the BankAccount class to include a SavingsAccount class with the ability to add interest.

# Sample Usage
savings_account2 = SavingsAccount("Charlie", 1000, interest_rate=0.03)

# Testing the new functionality
print(savings_account2.get_balance())  # Output: Current balance: $1000
print(savings_account2.add_interest())  # Output: Interest added. New balance: $1030.0

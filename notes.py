# Lesson 6: Object-Oriented Programming (OOP) - Summary Notes

# Brief Overview:
# In this lesson, we explore the fundamentals of Object-Oriented Programming (OOP) in Python.
# OOP allows us to model real-world objects and concepts as classes and objects. 
# This approach helps in structuring code for reusability, modularity, and scalability.

# Key Concepts Covered:

# 1. Classes and Objects:
# - A class is a blueprint for creating objects. It defines attributes (properties) 
#   and methods (functions) that the objects of the class will have.
# - An object is an instance of a class. It contains the actual data and behavior 
#   defined in the class.

# Example:
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

# 2. The `__init__` Method (Constructor):
# - The `__init__` method is the constructor in Python. It's called when an object 
#   is instantiated and is used to initialize the object's attributes.

# Example:
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# Creating an object of the Person class
person1 = Person("Alice", 25)
print(person1.name)  # Output: Alice
print(person1.age)   # Output: 25

# 3. Instance Attributes and Methods:
# - Instance attributes are variables that belong to an instance (object) of the class.
# - Instance methods are functions defined inside the class that operate on instance 
#   attributes.

# Example:
class BankAccount:
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return f"Deposited ${amount}. New balance: ${self.balance}"

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return f"Withdrew ${amount}. New balance: ${self.balance}"
        else:
            return "Insufficient funds."

# Creating an object of BankAccount
account = BankAccount("Alice", 100)
print(account.deposit(50))   # Output: Deposited $50. New balance: $150
print(account.withdraw(30))  # Output: Withdrew $30. New balance: $120

# 4. Class Attributes and Methods:
# - Class attributes are variables that belong to the class itself rather than 
#   to instances of the class.
# - Class methods are methods that operate on the class, not on an instance.

# Example:
class Dog:
    species = "Canine"  # Class attribute

    def __init__(self, name, age):
        self.name = name  # Instance attribute
        self.age = age    # Instance attribute

    def speak(self):
        return f"{self.name} says Woof!"

# Creating an object of the Dog class
dog = Dog("Buddy", 4)
print(dog.speak())  # Output: Buddy says Woof!
print(Dog.species)  # Output: Canine

# 5. Inheritance:
# - Inheritance allows one class (child class) to inherit the attributes and methods 
#   of another class (parent class).
# - This promotes code reuse and the creation of hierarchies.

# Example:
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} makes a sound"

# Inheriting from the Animal class
class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"

# Creating an object of the Dog class
dog = Dog("Buddy")
print(dog.speak())  # Output: Buddy says Woof!

# 6. Polymorphism:
# - Polymorphism allows objects of different classes to be treated as instances of the same class 
#   through a common interface.
# - Methods can be overridden in child classes, allowing different behavior for the same method.

# Example:
class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow!"

# Creating objects of different classes
animals = [Dog("Buddy"), Cat("Whiskers")]

for animal in animals:
    print(animal.speak())  
# Output:
# Buddy says Woof!
# Whiskers says Meow!

# 7. Encapsulation:
# - Encapsulation refers to bundling the data (attributes) and methods that operate on the data 
#   within a class, restricting access to some of the object's components.
# - This can be achieved by making attributes private (by prefixing with _ or __) and providing 
#   getter and setter methods.

# Example:
class Car:
    def __init__(self, make, model):
        self.__make = make  # Private attribute
        self.__model = model  # Private attribute

    def get_make(self):
        return self.__make

    def set_make(self, make):
        self.__make = make

# Creating an object of the Car class
car = Car("Toyota", "Corolla")
print(car.get_make())  # Output: Toyota
car.set_make("Honda")
print(car.get_make())  # Output: Honda

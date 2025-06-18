# 1. Using self
# Assignment:
# Create a class Student with attributes name and marks. Use the self keyword to initialize these values via a constructor. Add a method display() that prints student details.

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    def display(self):
        return(f'Name: {self.name}, Marks: {self.marks}')
student1: Student = Student('Alice', 85)
student2: Student = Student('Bob', 90)
print("Student 1 Details:", student1.display())
print(student1.name, student1.marks)
print("Student 2 Details:", student2.display())
print(student2.name, student2.marks)



# 2. Using cls
# Assignment:
# Create a class Counter that keeps track of how many objects have been created. Use a class variable and a class method with cls to manage and display the count.
class Counter:
    count = 0
    def __init__(self):
        Counter.count += 1

    @classmethod
    def display_count(cls):
            return f'Total objects created: {cls.count}'
obj1 : Counter = Counter()
obj2 : Counter = Counter()
obj3 : Counter = Counter()
print(Counter.display_count())



# 3. Public Variables and Methods
# Assignment:
# Create a class Car with a public variable brand and a public method start(). Instantiate the class and access both from outside the class.
class Car:
    def __init__(self, brand):
          self.brand = brand
    def start(self):
            return f'{self.brand} is starting.'
    
car: Car = Car("Toyota")
print(car.brand)
print(car.start())



# 4. Class Variables and Class Methods
# Assignment:
# Create a class Bank with a class variable bank_name. Add a class method change_bank_name(cls, name) that allows changing the bank name. Show that it affects all instances.
class Bank:
    bank_name = "Default Bank"

    @classmethod
    def cange_bank_name(cls, name):
        cls.bank_name = name

b1: Bank = Bank()
print(b1.bank_name)
b2:Bank = Bank()
print(b2.bank_name)
Bank.cange_bank_name("New Bank")
print(b1.bank_name)
print(b2.bank_name)



# 5. Static Variables and Static Methods
# Assignment:
# Create a class MathUtils with a static method add(a, b) that returns the sum. No class or instance variables should be used.
class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b 
print(MathUtils.add(5, 10))



# 6. Constructors and Destructors
# Assignment:
# Create a class Logger that prints a message when an object is created (constructor) and another message when it is destroyed (destructor).

class Logger:
    def __init__(self):
        print("Logger object created.")

    # def __del__(self):
    #     print("Logger object destroyed.")

log:Logger = Logger()
print(log)



# 7. Access Modifiers: Public, Private, and Protected
# Assignment:
# Create a class Employee with:

# a public variable name,

# a protected variable _salary, and

# a private variable __ssn.

# Try accessing all three variables from an object of the class and document what happens.

class Employee:
    def __init__(self, name, salary, ssn):
        self.name = name  # Public variable
        self._salary = salary  # Protected variable
        self.__ssn = ssn  # Private variable

emp1: Employee = Employee("Samra Moinuddin", 10000, "123-45-6789")
print(emp1.name)  # Accessing public variable
print(emp1._salary)  # Accessing protected variable (not recommended, but possible)
# print(emp1.__ssn)
print(emp1._Employee__ssn) # Attempting to access private variable (will raise an AttributeError)



# 8. The super() Function
# Assignment:
# Create a class Person with a constructor that sets the name. Inherit a class Teacher from it, add a subject field, and use super() to call the base class constructor.

class Person:
     def __init__(self, name):
        self.name = name

class Teacher(Person):
     def __init__(self, name, subject):
          super().__init__(name)
          self.subject = subject
teacher: Teacher = Teacher("Samra Moinuddin", "Computer Science")
print(f'Name: {teacher.name}, Subject: {teacher.subject}')



# 9. Abstract Classes and Methods
# Assignment:
# Use the abc module to create an abstract class Shape with an abstract method area(). Inherit a class Rectangle that implements area().
from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def area(self):
        return self.height* self.width
rect1: Rectangle = Rectangle(5.8, 10.6)
print(f'Area of Reactangle: {rect1.area()}')



# 10. Instance Methods
# Assignment:
# Create a class Dog with instance variables name and breed. Add an instance method bark() that prints a message including the dog's name.
class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        return f'{self.name} says Woofff! '
dog1: Dog = Dog("Tommy", "Labrador")
print(dog1.bark())



# 11. Class Methods
# Assignment:
# Create a class Book with a class variable total_books. Add a class method increment_book_count() to increase the count when a new book is added.
class Book:
    # Class variable to track total number of books
    total_books = 0

    def __init__(self, title):
        self.title = title
        # Call the class method to increment book count
        Book.increment_book_count()

    @classmethod
    def increment_book_count(cls):
        cls.total_books += 1

# Example usage:
book1 = Book("Python Basics")
book2 = Book("Data Structures")
book3 = Book("Web Development")

print("Total books added:", Book.total_books)




# 12. Static Methods
# Assignment:
# Create a class TemperatureConverter with a static method celsius_to_fahrenheit(c) that returns the Fahrenheit value.
class TemperatureConverter:
    @staticmethod
    def celsius_to_fahrenheit(c):
        return (c * 9/5) + 32

# Example usage:
temp_celsius = 25
temp_fahrenheit = TemperatureConverter.celsius_to_fahrenheit(temp_celsius)

print(f"{temp_celsius}°C is equal to {temp_fahrenheit}°F")



# 13. Composition
# Assignment:
# Create a class Engine and a class Car. Use composition by passing an Engine object to the Car class during initialization. Access a method of the Engine class via the Car class.
class Engine:
    def start(self):
        return "Engine has started."

class Car:
    def __init__(self, engine):
        self.engine = engine  # Composition: Engine is part of Car

    def start_car(self):
        return self.engine.start()  # Accessing Engine's method through Car

# Example usage:
my_engine = Engine()
my_car = Car(my_engine)

print(my_car.start_car())



# 14. Aggregation
# Assignment:
# Create a class Department and a class Employee. Use aggregation by having a Department object store a reference to an Employee object that exists independently of it.
class Employee:
    def __init__(self, name, emp_id):
        self.name = name
        self.emp_id = emp_id

    def get_details(self):
        return f"Employee Name: {self.name}, ID: {self.emp_id}"

class Department:
    def __init__(self, department_name, employee):
        self.department_name = department_name
        self.employee = employee  # Aggregation: storing reference

    def show_info(self):
        return f"Department: {self.department_name}\n{self.employee.get_details()}"

# Example usage:
emp1 = Employee("Samra", 101)
dept1 = Department("IT", emp1)

print(dept1.show_info())



# 15. Method Resolution Order (MRO) and Diamond Inheritance
# Assignment:
# Create four classes:

# A with a method show(),

# B and C that inherit from A and override show(),

# D that inherits from both B and C.

# Create an object of D and call show() to observe MRO.

class A:
    def show(self):
        print("Show from Class A")

class B(A):
    def show(self):
        print("Show from Class B")

class C(A):
    def show(self):
        print("Show from Class C")

class D(B, C):  # Diamond Inheritance
    pass

# Create object of class D
d = D()
d.show()

# To see the MRO order
print(D.__mro__)




# 16. Function Decorators
# Assignment:
# Write a decorator function log_function_call that prints "Function is being called" before a function executes. Apply it to a function say_hello().
# Decorator function
def log_function_call(func):
    def wrapper():
        print("Function is being called")
        return func()
    return wrapper

# Apply decorator
@log_function_call
def say_hello():
    print("Hello, Samra!")

# Call the function
say_hello()



# 17. Class Decorators
# Assignment:
# Create a class decorator add_greeting that modifies a class to add a greet() method returning "Hello from Decorator!". Apply it to a class Person.
# Class decorator to add a greet() method
def add_greeting(cls):
    def greet(self):
        return "Hello from Decorator!"
    
    # Add the greet method to the class
    cls.greet = greet
    return cls

# Apply the class decorator
@add_greeting
class Person:
    def __init__(self, name):
        self.name = name

# Example usage
p = Person("Samra")
print(p.greet())  # Output: Hello from Decorator!




# 18. Property Decorators: @property, @setter, and @deleter
# Assignment:
# Create a class Product with a private attribute _price. Use @property to get the price, @price.setter to update it, and @price.deleter to delete it.
class Product:
    def __init__(self, price):
        self._price = price  # private attribute

    @property
    def price(self):
        print("Getting the price...")
        return self._price

    @price.setter
    def price(self, value):
        print("Setting the price...")
        if value >= 0:
            self._price = value
        else:
            print("Invalid price! Price cannot be negative.")

    @price.deleter
    def price(self):
        print("Deleting the price...")
        del self._price

# Example usage:
p = Product(500)

print(p.price)       # Getting the price
p.price = 700        # Setting the price
print(p.price)       # Getting updated price

del p.price          # Deleting the price




# 19. callable() and __call__()
# Assignment:
# Create a class Multiplier with an __init__() to set a factor. Define a __call__() method that multiplies an input by the factor. Test it with callable() and by calling the object like a function.
class Multiplier:
    def __init__(self, factor):
        self.factor = factor

    def __call__(self, number):
        return number * self.factor

# Create an object of Multiplier
double = Multiplier(2)

# Test with callable()
print(callable(double))  # Output: True

# Call the object like a function
result = double(5)  # 5 * 2 = 10
print("Result:", result)



# 20. Creating a Custom Exception
# Assignment:
# Create a custom exception InvalidAgeError. Write a function check_age(age) that raises this exception if age < 18. Handle it with try...except.
# Step 1: Define a custom exception
class InvalidAgeError(Exception):
    pass

# Step 2: Define a function that checks age
def check_age(age):
    if age < 18:
        raise InvalidAgeError("Age must be at least 18 to proceed.")
    else:
        print("Age is valid. You may proceed.")

# Step 3: Handle the exception using try...except
try:
    user_age = int(input("Enter your age: "))
    check_age(user_age)
except InvalidAgeError as e:
    print("InvalidAgeError:", e)
except ValueError:
    print("Please enter a valid number.")




# 21. Make a Custom Class Iterable
# Assignment:
# Create a class Countdown that takes a start number. Implement __iter__() and __next__() to make the object iterable in a for-loop, counting down to 0.

class Countdown:
    def __init__(self, start):
        self.current = start

    def __iter__(self):
        return self  # Iterator object itself

    def __next__(self):
        if self.current < 0:
            raise StopIteration  # End of iteration
        value = self.current
        self.current -= 1
        return value

# Example usage:
for number in Countdown(5):
    print(number)

from datetime import date

class Student:
    # Class Attributes are variables that are part of a class
    # They are shared by all instances of a class
    # They are defined outside of any method
    # They are accessed using the class name
    # They are useful for defining constants
    school = "University of Toronto"
    no_of_students = 0

    # Constructor
    # This is called when an object is created
    # Self is a reference to the object itself
    # def is a keyword that defines a function or method
    # __init__ is a special method that is called when an object is created
    # It is used to initialize the object's attributes 
    # age=0 is a default value for the age parameter
    # courses='none' is a default value for the courses parameter to avoid errors
    def __init__(self, name, age=0, courses='none'):
        # Instance Attributes are variables that are part of an Instance
        # self.name is an instance attribute and its public because it can be accessed outside the class
        # self.__age is a private instance attribute and it can only be accessed within the class
        self.__name = name
        self.__age = age
        self.__courses = courses
        Student.no_of_students += 1

    

    #######################################
    # there is 3 types of methods in python
    #######################################


    # 1. Instance Methods
    #====================  
    # this type of method takes self as a parameter and can access the instance attributes
    # It can be called on an object to get a string representation of the object
    
    # Dunnder methods
    #================
    #  are special methods that have double underscores at the beginning and end of their names
    # They are also called magic methods\special methods
    # They are automatically called by python when certain operations are performed
    # we can override them to define custom behaviour for our objects
    def __str__(self):
        # (f) strings are a way to format strings in python to inject variables
        return f"{self.__name} is {self.__age} years old and is taking {self.__courses}" 
    
    # It can be called on an object to get a string representation of the object
    def __repr__(self):
        # .format() is a method that replaces placeholders in a string with variables
        return "Student('{}', {})".format(self.__name, self.__age)
    
    # Setter Method are instance methods that set the value of an attribute
    # This is a method that sets the value of an attribute
    # It takes self and the new value as parameters
    def set_age(self, age):
        self.__age = age

    def set_courses(self, courses):
        self.__courses = courses
    
    def set_name(self, name):
        self.__name = name

    
    # Getter Method are instance methods that get the value of an attribute
    # This is a method that gets the value of an attribute
    # It takes self as a parameter
    def get_age(self):
        return self.__age
    
    def get_courses(self):
        return self.__courses
    
    def get_name(self):
        return self.__name
    
    ################################################################################

    # 2. Class Methods
    #====================
    # Class Methods are methods that are bound to the class rather than the object
    # They take cls as a parameter which refers to the class itself
    # They can be called on the class to get or set class attributes
    # They are defined using the @classmethod decorator
    @classmethod
    def get_no_of_students(cls):
        return cls.no_of_students
    
    @classmethod
    def init_from_birth_year(cls, name, birth_year,courses='none'):
        # it works as a constructor but it is a class method
        # it returns an object of the class with the given parameters
        return cls(name, date.today().year - birth_year, courses)
    
    ################################################################################

    # 3. Static Methods
    #====================
    # Static Methods are methods that are not bound to the class or the object
    # They do not take self or cls as a parameter
    # They are defined using the @staticmethod decorator
    @staticmethod
    def is_adult(age):
        return age > 18
    
    @staticmethod
    def is_teen(age):
        return age > 12 and age < 20
    
    @staticmethod
    def is_senior(age):
        return age > 60
    
    


    

# Create an object of the class
student_1 = Student("Alice",8)

student_2 = Student("Bob", 21, ["CSC108", "CSC148", "CSC165"])

# Access the class attribute by setter method

print (student_1.get_name())

student_1.set_name("Alice Smith")

print (student_1.get_name())

# Does not work because it is a private attribute
# Does not give an error because it creates a new attribute in the class
student_1.age = 10
print (student_1.age)

print (student_1)
print (student_2)

# use the class method to create an object
student_3 = Student.init_from_birth_year("Charlie", 2000, ["CSC108", "CSC148", "CSC165"])
print(student_3)

# Access the class attribute by class method
print(f"Number of students: {Student.get_no_of_students()}")

# test the static methods can be called without creating an object of the class
print(Student.is_adult(20))
print(Student.is_teen(55))
print(Student.is_senior(70))

#############################################################
# Example for Inheritance
#############################################################
class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
    
    def get_name(self):
        return self.__name
    
    def get_age(self):
        return self.__age
    
    def set_name(self, name):
        self.__name = name
    
    def set_age(self, age):
        self.__age = age
    
    def display(self):
        return f"{self.__name} is {self.__age} years old"

# Inheritance is a way to create a new class using an existing class
# The new class is called a subclass or derived class
# The existing class is called a superclass or base class
# The subclass inherits the attributes and methods of the superclass
class Teacher(Person):
    
    no_of_teachers = 0

    def __init__(self, name, age, salary):
        # super() is a function that returns the parent class
        # It is used to call the parent class constructor
        super().__init__(name, age)
        self.__salary = salary
        Teacher.no_of_teachers += 1
    
    def get_salary(self):
        return self.__salary
    
    def set_salary(self, salary):
        self.__salary = salary

    #Polymorphism
    #====================
    # Overriding is a way to change the behaviour of a method in the subclass
    # It is done by defining a method with the same name in the subclass
    # The method in the subclass overrides the method in the superclass
    def display(self):
        return f"{super().display()} and earns {self.__salary} per year"

class trainee_teacher(Person):
    no_of_trainee_teachers = 0
    def __init__(self, name, age, hours):
        super().__init__(name, age)
        self._hours = hours
        trainee_teacher.no_of_trainee_teachers += 1
    
    def get_hours(self):
        return self._hours
    
    def set_hours(self, hours):
        self._hours = hours

    #Polymorphism
    #====================
    # Overriding is a way to change the behaviour of a method in the subclass
    # It is done by defining a method with the same name in the subclass
    # The method in the subclass overrides the method in the superclass
    def display(self):
        return f"{super().display()} and works {self._hours} hours a week"

# Create an object of the subclass
teacher_1 = Teacher("Alice", 30, 60000)
teacher_2 = Teacher("Bob", 40, 70000)

print(teacher_1.display())
print(teacher_2.display())
print(f"Number of teachers: {Teacher.no_of_teachers}")

trainee_teacher_1 = trainee_teacher("Charlie", 25, 20)
trainee_teacher_2 = trainee_teacher("David", 26, 25)

print(trainee_teacher_1.display())
print(trainee_teacher_2.display())
print(f"Number of trainee teachers: {trainee_teacher.no_of_trainee_teachers}")

print(isinstance(teacher_1, Student))


#############################################################
# Example for Abstract Base Class

from abc import ABC, abstractmethod

# Abstract Base Class is a class that cannot be instantiated
# It is used to define a blueprint for other classes
# It is used to define abstract methods that must be implemented by subclasses

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    
    @abstractmethod
    def perimeter(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.__radius = radius
    
    def area(self):
        return 3.14 * self.__radius * self.__radius
    
    def perimeter(self):
        return 2 * 3.14 * self.__radius

class Rectangle(Shape):
    def __init__(self, length, width):
        self.__length = length
        self.__width = width
    
    def area(self):
        return self.__length * self.__width
    
    def perimeter(self):
        return 2 * (self.__length + self.__width)


circle = Circle(5)
rectangle = Rectangle(5, 10)

print(f"Circle Area: {circle.area()}")
print(f"Circle Perimeter: {circle.perimeter()}")
print(f"Rectangle Area: {rectangle.area()}")
print(f"Rectangle Perimeter: {rectangle.perimeter()}")



#############################################################
# More Examples for Duunder Methods
#############################################################
class Man:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
    
    def __str__(self):
        return f"{self.__name} is {self.__age} years old"
    
    def __add__(self, other):
        names = self.__name + " " + other.__name
        ages = self.__age + other.__age
        return f"names are {names} and ages are {ages}"
    # Overloading the less than operator to compare the ages of two objects
    def __lt__(self, other):
        return self.__age < other.__age
    
    

man_1=Man("Ali", 30)
man_2=Man("Ahmed", 40)

print(man_1+man_2)

print(man_1>man_2)
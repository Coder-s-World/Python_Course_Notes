This reading introduces you to the OOP principles in more detail using some examples.

The object oriented paradigm was introduced in the 1960s by Alan Kay. At the time, the paradigm was not the best computing solution given the small scalability of software developed then. As the complexity of software and real-life applications improved, object oriented principles became a better solution. 

You previously encountered the four main pillars of object oriented programming. These are:  encapsulation, polymorphism, inheritance and abstraction. Let's look at a few examples that demonstrate how these principles translate when using Python.

Encapsulation
The idea of encapsulation is to have methods and variables within the bounds of a given unit. In the case of Python, this unit is called a class. And the members of a class become locally bound to that class. These concepts are better understood with scope, such as global scope (which in simple terms is the files I am working with), and local scope (which refers to the method and variables that are 'local' to a class). Encapsulation thus helps in establishing these scopes to some extent. 

For example, the Little Lemon company may have different departments such as inventory, marketing and accounts. And you may be required to deal with the data and operations for each of them separately. Classes and objects help in encapsulating and in turn restrict the different functionalities.

Encapsulation is also used for hiding data and its internal representation. The term for this is information hiding.  Python has a way to deal with it, but it is better implemented in other programming languages such as Java and C++. Access modifiers represented by keywords such as public, private and protected are used for information hiding. The use of single and double underscores for this purpose in Python is a substitute for this practice. For example, let's examine an example of protected members in Python.


class Alpha:
    
    def __init__(self):
        self._a = 2.  # Protected member ‘a’
        self.__b = 2.  # Private member ‘b’

self._a is a protected member and can be accessed by the class and its subclasses.

Private members in Python are conventionally used with preceding double underscores: __. self.__b is a private member of the class Alpha and can only be accessed from within the class Alpha.

It should be noted that these private and protected members can still be accessed from outside of the class by using public methods to access them or by a practice known as name mangling. Name mangling is the use of two leading underscores and one trailing underscore, for example:

_class__identifier

Class is the name of the class and identifier is the data member that I want to access.

Polymorphism
Polymorphism refers to something that can have many forms. In this case, a given object. Remember that everything in Python is inherently an object, so when I talk about polymorphism, it can be an operator, method or any object of some class. I can illustrate the case for polymorphism using built-in functions and operations, for example:


string = "poly"
num = 7
sequence = [1,2,3]
new_str = string * 3
new_num = 7 * 3
new_sequence = sequence * 3

print(new_str, new_num, new_sequence)

The output is:
polypolypoly 21 [1, 2, 3, 1, 2, 3, 1, 2, 3]

In this case, the * operator exhibits polymorphism. It works differently depending on the type of object it's applied to:

  When applied to a string, it repeats the string.
  When applied to an integer, it performs multiplication.
  When applied to a list, it repeats the list.

This is an example of polymorphism because the same operator * is behaving differently depending on the type of object.

Let's examine one more example.

string = "poly"
sequence = [1,2,3]
print(len(string))
print(len(sequence))

The output is:
4
3

In this example, the len() function is polymorphic because it calculates the length of different types of objects:
  For the string "poly", it returns 4 because there are 4 characters in the string.
  For the list [1, 2, 3], it returns 3 because there are 3 elements in the list.
Despite len() being the same function, it works differently depending on the type of the object passed to it.

Inheritance
Inheritance is a fundamental concept in object-oriented programming (OOP) that allows a class (called a child or derived class) to inherit attributes and methods from another class (called a parent or base class).

Here, a parent class Animal is created that has a method info(). Then a child classes Dog is created that inherit from Animal and add their own behavior.


class Animal:
    def __init__(self, name):
        self.name = name
​
    def info(self):
        print("Animal name:", self.name)
​
class Dog(Animal):
    def sound(self):
        print(self.name, "barks")
​
d = Dog("Buddy")

# Inherited method
d.info()     
d.sound()

Output
Animal name: Buddy
Buddy barks
Explanation:

class Animal defines the parent class.
info() prints the name of the animal.
class Dog(Animal) defines Dog as a child of Animal class.
d.info() calls parent method info() and d.sound() calls child method.
animal_class
    
Inheritance in Python
Why do we need Inheritance
     *   Promotes code reusability by sharing attributes and methods across classes.
     *   Models real-world hierarchies like Animal -> Dog or Person -> Employee.
     *   Simplifies maintenance through centralized updates in parent classes.
     *   Enables method overriding for customized subclass behavior.
     *   Supports scalable, extensible design using polymorphism.
    
super() Function
super() function is used to call methods from a superclass following Python’s Method Resolution Order (MRO). In particular, it is commonly used in the child class's __init__() method to initialize inherited attributes. This way, the child class can leverage the functionality of the parent class.

Example: Here, Dog uses super() to call Animal's constructor

# Parent Class: Animal
class Animal:
    def __init__(self, name):
        self.name = name
​
    def info(self):
        print("Animal name:", self.name)
​
# Child Class: Dog
class Dog(Animal):
    def __init__(self, name, breed):
        # Calls constructor based on MRO
        super().__init__(name)  
        self.breed = breed
​
    def details(self):
        print(self.name, "is a", self.breed)
​
d = Dog("Buddy", "Golden Retriever")
d.info()      # Parent method
d.details()   # Child method

Output
Animal name: Buddy
Buddy is a Golden Retriever
Explanation:

super() function is used inside __init__() method of Dog to call the constructor of Animal and initialize inherited attribute (name).
This ensures that parent class functionality is reused without needing to rewrite the code in the child class.

class Parent:
    Members of the parent class

class Child(Parent):
    Inherited members from parent class
    Additional members of the child class

As the structure of inheritance gets more complicated, Python adheres to something called the Method Resolution Order (MRO) that determines the flow of execution. MRO is a set of rules, or an algorithm, that Python uses to implement monotonicity, which refers to the order or sequence in which the interpreter will look for the variables and functions to implement. This also helps in determining the scope of the different members of the given class.
Types of Inheritance in Python

Inheritance is an Object-Oriented Programming (OOP) feature that allows one class to acquire the properties and methods of another class.

Benefits of Inheritance
Code Reusability
Easy Maintenance
Better Organization
Supports Hierarchical Relationships
1. Single Inheritance

A child class inherits from one parent class.

Parent
   │
   ▼
Child
Example
class Animal:
    def sound(self):
        print("Animal makes sound")

class Dog(Animal):
    pass
2. Multiple Inheritance

A child class inherits from more than one parent class.

Parent1      Parent2
    \          /
     \        /
      ▼      ▼
        Child
Example
class Father:
    pass

class Mother:
    pass

class Child(Father, Mother):
    pass
    When a class inherits from more than one base class, it is called multiple inheritance. The derived class inherits all features of its base classes.

frame_3319
Syntax:
class Base1:
     # Body of the class
        pass

class Base2:
    # Body of the class
        pass

class Derived(Base1, Base2):
         # Body of the class
         pass 

The Diamond Problem
Diamond Problem occurs when two classes inherit from a common superclass, and another class inherits from both. If a method is overridden in the intermediate classes, ambiguity arises about which method the derived class should use.

frame_3320
Class1 is the base, Class2 and Class3 inherit from it, Class4 inherits from both.
Calling a method overridden in Class2 and Class3 creates ambiguity.
Python uses MRO to resolve it and ensure a consistent call sequence.
Python have a built-in solution to the Diamond Problem, and it's handled through the Method Resolution Order (MRO) using the C3 linearization algorithm.

Method Resolution Order
Method Resolution Order (MRO) in Python determines the order in which base classes are searched when looking for an attribute in multiple inheritance. It follows a linearization rule: the current class is checked first, then parent classes are searched from left to right, each class only once. You can view it using:

Class.mro()-> returns a list
Class.__mro__ -> returns a tuple
The below code demonstrates the use of super() with multiple inheritance: calling obj.m() executes the m methods following the Method Resolution Order (MRO), ensuring each parent method is called once. The mro() and __mro__ outputs show the search order: Class4 -> Class2 -> Class3 -> Class1 -> object.

class Class1:
    def m(self):
        print("In Class1")
​
class Class2(Class1):
    def m(self):
        print("In Class2")
        super().m()
​
class Class3(Class1):
    def m(self):
        print("In Class3")
        super().m()
​
class Class4(Class2, Class3):
    def m(self):
        print("In Class4")   
        super().m()
     
print(Class4.mro())         
print(Class4.__mro__)

Output
[<class '__main__.Class4'>, <class '__main__.Class2'>, <class '__main__.Class3'>, <class '__main__.Class1'>, <class 'object'>]
(<class '__main__.Class4'>, <class '__main__.Class2'>, <class '__main__.C...
Example 1: When the method is overridden in both classes
The code demonstrates multiple inheritance where Class4 inherits from Class2 and Class3; calling obj.m() executes Class2’s method because, according to Python’s MRO, Class2 is checked before Class3.

class Class1:
    def m(self):
        print("In Class1") 
      
class Class2(Class1):
    def m(self):
        print("In Class2")
​
class Class3(Class1):
    def m(self):
        print("In Class3")  
       
class Class4(Class2, Class3):
    pass   
    
obj = Class4()
obj.m()

Output
In Class2

Example 2: When the Method overridden in one class only
The code shows multiple inheritance where Class4 inherits from Class2 and Class3; calling obj.m() executes Class3’s method due to Python’s method resolution order (MRO).

class Class1:
    def m(self):
        print("In Class1")
​
class Class2(Class1):
    pass
​
class Class3(Class1):
    def m(self):
        print("In Class3")
​
class Class4(Class2, Class3):
    pass
​
obj = Class4()
obj.m()

Output
In Class3

Example 3: All classes define the same method
The code demonstrates multiple inheritance, showing that Class4 overrides the m method, but methods from parent classes (Class2, Class3, Class1) can still be called explicitly using the class name.

class Class1:
    def m(self):
        print("In Class1")
​
class Class2(Class1):
    def m(self):
        print("In Class2")
​
class Class3(Class1):
    def m(self):
        print("In Class3")
​
class Class4(Class2, Class3):
    def m(self):
        print("In Class4")
​
obj = Class4()
obj.m()
Class2.m(obj)
Class3.m(obj)
Class1.m(obj)

Output
In Class4
In Class2
In Class3
In Class1

Example 4: Calling methods of parent classes from child class
The code demonstrates multiple inheritance and explicitly calls parent class methods, showing how Class1.m() is invoked multiple times through Class2 and Class3.

class Class1:
    def m(self):
        print("In Class1")
​
class Class2(Class1):
    def m(self):
        print("In Class2")
        Class1.m(self)
​
class Class3(Class1):
    def m(self):
        print("In Class3")
        Class1.m(self)
​
class Class4(Class2, Class3):
    def m(self):
        print("In Class4")
        Class2.m(self)
        Class3.m(self)
​
obj = Class4()
obj.m()

Output
In Class4
In Class2
In Class1
In Class3
In Class1

Super Function 
Super Function in Python is used to call a method from a parent (base) class, especially in multiple inheritance. It helps avoid explicitly naming the parent class, ensures proper method resolution following the MRO, and prevents duplicate calls of the same method.

class Class1:
    def m(self):
        print("In Class1")
​
class Class2(Class1):
    def m(self):
        print("In Class2")
        super().m()
​
class Class3(Class1):
    def m(self):
        print("In Class3")
        super().m()
​
class Class4(Class2, Class3):
    def m(self):
        print("In Class4")   
        super().m()
     
obj = Class4()
obj.m()

Output
In Class4
In Class2
In Class3
In Class1

Explanation:
  *  Class4 inherits from Class2 and Class3, which both inherit from Class1, forming a diamond.
  *  Each class defines its own m() method.
  *  super() calls the next method in the Method Resolution Order (MRO).
  *  MRO for Class4 is Class4 -> Class2 -> Class3 -> Class1.
  *  Calling obj.m() executes the methods in MRO order.

3. Multilevel Inheritance

A class inherits from a class that is already inherited from another class.

Grandparent
      │
      ▼
   Parent
      │
      ▼
    Child

Example
class Grandparent:
    pass

class Parent(Grandparent):
    pass

class Child(Parent):
    pass
    
4. Hierarchical Inheritance

Multiple child classes inherit from the same parent class.

        Parent
       /   |   \
      ▼    ▼    ▼
   Child1 Child2 Child3
Example
class Animal:
    pass

class Dog(Animal):
    pass

class Cat(Animal):
    pass

class Cow(Animal):
    pass
5. Hybrid Inheritance

A combination of two or more inheritance types.

       A
      / \
     ▼   ▼
     B   C
      \ /
       ▼
       D
Example
class A:
    pass

class B(A):
    pass

class C(A):
    pass

class D(B, C):
    pass

Hybrid inheritance combines:

Multiple Inheritance
Multilevel Inheritance
Hierarchical Inheritance

Summary Table
| Type                     | Description                               | Structure       |
| ------------------------ | ----------------------------------------- | --------------- |
| Single Inheritance       | One child inherits from one parent        | A → B           |
| Multiple Inheritance     | One child inherits from multiple parents  | A, B → C        |
| Multilevel Inheritance   | Inheritance in multiple levels            | A → B → C       |
| Hierarchical Inheritance | Multiple children inherit from one parent | A → B, C, D     |
| Hybrid Inheritance       | Combination of inheritance types          | Mixed Structure |


Abstraction
Abstraction can be seen both as a means for hiding important information as well as unnecessary information in a block of code. The core of abstraction in Python is the implementation of something called abstract classes and methods, which can be implemented by inheriting from something called the abc module. abc here stands for abstract base class. It is first imported and then used as a parent class for some class that becomes an abstract class. Its simplest implementation can be done as below.

from abc import ABC,   
class ClassName(ABC):
    pass

Data abstraction means showing only the essential features and hiding the complex internal details. It is used to hide the implementation details from the user and expose only necessary parts, making the code simpler and easier to interact with.

data_abstraction
Data Abstraction in Python
Real Life Example: In a graphics software, multiple shapes are available such as Circle, Rectangle and Triangle. All shapes share common data and support the same set of actions, but the internal details are hidden:

Common data: name, color, border thickness, fill style.
Common actions: draw(), resize(), getArea().
Each shape implements these actions differently Circle uses radius, Rectangle uses length and width and Triangle uses base and height.
The software only knows that a shape can be drawn and its area can be calculated. How the shape is drawn or how the area is calculated is hidden.

Abstract Base Class
Abstract Base Class (ABC) is used to achieve data abstraction by defining a common interface for its subclasses. It cannot be instantiated directly and serves as a blueprint for other classes.

Abstract classes are created using abc module and @abstractmethod decorator, allowing developers to enforce method implementation in subclasses while hiding complex internal logic.

from abc import ABC, abstractmethod
​
class Greet(ABC):
    @abstractmethod
    def say_hello(self):
        pass  # Abstract method
​
class English(Greet):
    def say_hello(self):
        return Hello!
​
    
g = English()
print(g.say_hello())

Output
Hello!

Explanation:

Greet is an abstract class with a method say_hello() that has no implementation.
English implements this method and returns a greeting.
This keeps structure fixed while letting subclasses define their own behavior.

Components of Abstraction
Abstraction is made up of key components, these elements work together to define a clear and enforced structure for subclasses while hiding unnecessary implementation details. Let's discuss them one by one.

1. Abstract Method
   Abstract methods are method declarations without a body defined inside an abstract class. They act as placeholders that force subclasses to provide their      own specific implementation, ensuring consistent structure across derived classes.

from abc import ABC, abstractmethod
     
class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass  # Abstract method, no implementation here
        
Explanation: make_sound() is an abstract method in Animal class, so it doesn't have any code inside it.

2. Concrete Method
   Concrete methods are fully implemented methods within an abstract class. Subclasses can inherit and use them directly, promoting code reuse without needing    to redefine common functionality.

from abc import ABC, abstractmethod
class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass  # Abstract method, to be implemented by subclasses
​
    def move(self):
        return "Moving"  # Concrete method with implementation
Explanation: move() method is a concrete method in Animal class. It is implemented and does not need to be overridden by Dog class.

3. Abstract Properties
   Abstract properties work like abstract methods but are used for properties. These properties are declared with @property decorator and marked as abstract      using @abstractmethod. Subclasses must implement these properties.

from abc import ABC, abstractmethod
​
class Animal(ABC):
    @property
    @abstractmethod
    def species(self):
        pass  # Abstract property, must be implemented by subclasses
​
class Dog(Animal):
    @property
    def species(self):
        return Canine
​
# Instantiate the concrete subclass
dog = Dog()
print(dog.species)

Output
Canine

Explanation:
    species is an abstract property in Animal class and it is marked as @abstractmethod.
    Dog class implements species property, making it a concrete subclass that can be instantiated.
    Abstract properties enforce that a subclass provides property’s implementation.

4. Abstract Class Instantiation
   Abstract classes cannot be instantiated directly. This is because they contain one or more abstract methods or properties that lack implementations.           Attempting to instantiate an abstract class results in a TypeError.

from abc import ABC, abstractmethod
​
class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass
​
animal = Animal()

Explanation:
    Animal class is abstract because it has make_sound() method as an abstract method.
    Instantiating Animal() raises a TypeError because abstract classes with unimplemented methods can't be instantiated, only fully implemented subclasses can.


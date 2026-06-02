Class methods and static methods are special types of methods in Python that are bound to a class rather than its instances. They are used when behavior logically belongs to the class but does not always require access to instance-specific data.

Class Method
A class method is a method that receives the class itself as the first argument, conventionally named cls. It can access and modify class-level data and is often used to define factory methods. A factory method is a method that creates and returns an object of the class. It acts as an alternative constructor, allowing objects to be created in different ways.

Below is the syntax of class method:

class C:
    @classmethod
    def method(cls, arg1, arg2, ...):
        pass

Parameters:

cls: Reference to the class (automatically passed)
arg1, arg2, ...: Additional arguments as required

Example: This example uses a class method as a factory method to create an object using a birth year instead of directly passing age.

from datetime import date
​
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
​
    @classmethod
    def from_birth_year(cls, name, year):
        return cls(name, date.today().year - year)
​
p = Person.from_birth_year("Jake", 2000)
print(p.name)
print(p.age)

Output
Jake
26
Explanation: @classmethod allows from_birth_year() to receive cls and cls(name, age) creates a new object of the class.

Static Method
A static method is a method that does not receive self or cls automatically. It behaves like a normal function but is placed inside a class because it logically belongs there. It cannot access or modify class or instance data directly.
A utility function is a helper function that performs a task related to the class but does not depend on class-level or instance-level data.

Below is the syntax of static method:

class C:
    @staticmethod
    def method(arg1, arg2, ...):
        pass

Parameters:

arg1, arg2, ...: Regular function parameters
No self or cls is passed automatically

Example: This example defines a utility function inside a class to check whether a person is an adult.


class Person:
    def __init__(self, age):
        self.age = age
​
    @staticmethod
    def is_adult(age):
        return age >= 18
​
print(Person.is_adult(20))
p = Person(16)
print(p.is_adult(p.age))

Output
True
False
Explanation: @staticmethod defines is_adult() as a utility function. It does not access self or cls, and works only with the provided parameter age.

Class method vs Static Method
The key difference between a class method and a static method is whether the method needs access to the class itself.

| Feature                      | Static Method                                                                | Class Method                                                                  |                                                                              |  
| Definition                   | A method that belongs to a class but does not access class or instance data. | A method that belongs to a class and can                                      |                                                                              |    access or modify class-level data. 
| Decorator Used               | `@staticmethod`                                                              | `@classmethod`                                                                |                                                                              |
| First Parameter              | No special first parameter required.                                         | First parameter must be `cls`.                                                |                                                                              |
| Access to Class Variables    | ❌ Cannot directly access class variables using `cls`.                       | ✅ Can access class variables through `cls`.                                 |                                                                              |
| Access to Instance Variables | ❌ Cannot access instance variables directly.                                | ❌ Cannot access instance variables directly                                 |                                                                              |    unless an object is passed.     
| Access to Class Object       | ❌ No access to the class object.                                            | ✅ Receives the class object through `cls`.                                  |                                                                              |      
| Purpose                      | Utility/helper methods related to the class.                                 | Methods that work with class-level data.                                      |                                                                              |
| Can Modify Class Variables   | ❌ No                                                                        | ✅ Yes                                                                       |                                                                              |
| Can Create Class Objects     | ❌ Generally not used for this purpose.                                      | ✅ Commonly used as factory methods.                                         |                                                                               |
| Inheritance Support          | Works with inheritance but has no knowledge of which class called it.        | Aware of the class that called it through                                     |                                                                              | `cls`.                            
| Memory Dependency            | Independent of class state.                                                  | Dependent on class state.                                                     |                                                                              |
| Object Creation Required     | No                                                                           | No                                                                            |                                                                              |
| Best Use Case                | Helper functions, calculations, validations, utility operations.             | Managing class variables, alternative                                                                                                                          constructors, factory methods.        

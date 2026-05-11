
*args` and `**kwargs` in Python 

In Python, `*args` and `**kwargs` are used in functions when you want to accept **multiple arguments** without knowing in advance how many arguments the user will pass.

They make functions **flexible** and reusable.

1. What is `*args`?

`args` stands for **Arguments**.
`*args` allows a function to accept **multiple positional arguments**.

Syntax :-
def function_name(*args):
    pass

What are Positional Arguments?
Arguments passed according to their **position**.

Example:

def add(a, b):
    print(a + b)

add(10, 20)

Here:

* `10` goes to `a`
* `20` goes to `b`

because of position.

# Example of `*args`
def numbers(*args):
    print(args)

numbers(1, 2, 3, 4)

## Output
(1, 2, 3, 4)

# Important Point
`*args` stores values in a **tuple**.

Type check:
def test(*args):
    print(type(args))

test(1, 2, 3)

## Output
<class 'tuple'>

# How `*args` Works
When many positional values are passed:
numbers(10, 20, 30, 40)

Python converts them into:
args = (10, 20, 30, 40)

# Accessing Values from `*args`
def show(*args):
    print(args[0])
    print(args[1])

show(100, 200, 300)

## Output
100
200

# Looping Through `*args`
def display(*args):
    for i in args:
        print(i)

display(1, 2, 3, 4)

## Output
1
2
3
4

# Real Example of `*args`
## Sum of Numbers

def add(*numbers):
    total = 0

    for i in numbers:
        total += i

    print(total)

add(10, 20)
add(10, 20, 30)
add(1, 2, 3, 4, 5)

## Output
30
60
15

Why Use `*args`?

Use `*args` when:
  * Number of inputs is unknown
  * Flexible functions are needed
  * Multiple positional arguments are required

What are Keyword Arguments?

Arguments passed using names.

Example:

def student(name, age):
    print(name)
    print(age)

student(name = "Python", age=20)

What are Keyword Arguments?
Arguments passed using names.

Example:
def student(name, age):
    print(name)
    print(age)

student(name = "Python", age=20)

Here:
name = "Ludhiana"
age=20  are keyword arguments.

Example of **kwargs
def details(**kwargs):
    print(kwargs)

details(name = "Python", age = 20)

Output
{'name': 'Python', 'age': 20}

Important Point
**kwargs stores data in a dictionary.

Type check:
def test(**kwargs):
    print(type(kwargs))

test(a=1, b=2)
Output
<class 'dict'>
How **kwargs Works

When you pass:
details(name="Python", age=20)

Python converts it into:
kwargs = {
    "name": "Python",
    "age": 20
}

Accessing Values from **kwargs
def info(**kwargs):
    print(kwargs["name"])

info(name="Python", age=25)
Output
Rahul

Looping Through **kwargs
def student(**kwargs):
    for key, value in kwargs.items():
        print(key, value)

student(name="Python", age=20, city="Ludhiana")
Output
name Python
age 20
city Ludhiana

Why Use **kwargs?
Use **kwargs when:

Number of keyword arguments is unknown
Flexible named inputs are needed
Dynamic data handling is required

Difference Between *args and **kwargs
| Feature         | `*args`              | `**kwargs`        |
| --------------- | -------------------- | ----------------- |
| Full Form       | Arguments            | Keyword Arguments |
| Accepts         | Positional Arguments | Keyword Arguments |
| Symbol          | `*`                  | `**`              |
| Stores Data In  | Tuple                | Dictionary        |
| Arguments Style | Normal values        | key=value         |
| Example         | `(1,2,3)`            | `{"a":1,"b":2}`   |

                                 
def demo(*args, **kwargs):
    print(args)
    print(kwargs)

demo(1, 2, 3, name="Python", age=20)
Output
(1, 2, 3)
{'name': 'Python', 'age': 20}

Order Rules in Function Parameters
Correct order:
def func(normal, *args, **kwargs):
    pass

Order should be:
Normal parameters
*args
**kwargs

Example with All Types
def student(name, *marks, **details):
    print(name)
    print(marks)
    print(details)

student(
    "Python",
    90,
    85,
    88,
    age=20,
    city="ludhiana"
)

# Output
Mayuri
(90, 85, 88)
{'age': 20, 'city': 'Ludhiana'}

Important Notes
1. Names args and kwargs are not compulsory

You can write:
def test(*x):
    print(x)
and
def test(**y):
    print(y)

But args and kwargs are standard conventions.

2. Single * and Double ** Matter
*args = means tuple packing.
**kwargs = means dictionary packing.

Packing and Unpacking

Packing
Collecting multiple values into one variable.

def test(*args):
    print(args)
Unpacking with *
numbers = [1, 2, 3]

print(*numbers)
Output
1 2 3

Unpacking with **
data = {
    "name": "Python",
    "age": 20
}

def student(name, age):
    print(name, age)

student(**data)
Output
Mayuri 20

Real-Life Use Cases
| Use Case             | Why Use                  |
| -------------------- | ------------------------ |
| Calculator Functions | Unknown number of inputs |
| APIs                 | Dynamic parameters       |
| Frameworks           | Flexible configuration   |
| Libraries            | Reusable functions       |
| Data Processing      | Variable user input      |


Common Mistakes

Mistake 1
def test(**kwargs, *args):
Wrong order.

Mistake 2
test(name)
for **kwargs
Wrong because keyword required.

Correct:
test(name="Python")

Simple Memory Trick
Symbol	Think
*args	Many values
**kwargs	Many named values


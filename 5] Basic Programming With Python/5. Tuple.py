"""Tuple
Tuple is an immutable ordered collection elements.
•	Tuples are similar to lists, but unlike lists, they cannot be changed after their creation.
•	Can hold elements of different data types.
•	These are ordered, heterogeneous and immutable.
👉 It is:
•	Ordered → elements keep their position 
•	Immutable → cannot be changed after creation 
•	Indexed → each element has an index
•	Allows Duplicates
🧠 Easy Way to Remember
•	Packing → many values → one tuple . Packing means putting multiple values into a single tuple.
•	Unpacking → one tuple → many variables (👉 Number of variables must match number of elements:) Unpacking means extracting values from a tuple into separate variables.

Creating  a tuple"""
# tuple
# create a tuple

# tuple_name = (element1, element2, element3)
tup = (1,2,3,4)

# Without parentheses (tuple packing)
t = 1, 2, 3

# Single element tuple (important!)
t = (5,)   # comma is required without it is considered as int

# empty tuple
t = ()

# Using tuple() constructor
t = tuple([1, 2, 3])   # from list
# Creating a Tuple with Mixed Datatypes
tup = (5, 'Welcome', 7.5, True, [1, 2, 3], {'key': 'value'})
print(tup)

"""Tuple Basic Operations
Accessing of Tuples
We can access the elements of a tuple by using indexing and slicing, similar to how we access elements in a list. Indexing starts at 0 for the first element and goes up to n-1, where n is the number of elements in the tuple. Negative indexing starts from -1 for the last element and goes backward.
# accessing the tuple"""

tup = (5,8,9)
print(tup[0])
print(tup[0:2])
print(tup[:])
print(tup[:-1])

tup1= tuple("hello",)
print(type(tup1))

#packing of tuple
tup2 = "hi","u","y"
print(type(tup2))

#unpacking of tuple
a,b,c=tup2

print(a)
print(b)
print(c)

"""Concatenation of Tuples
Tuples can be concatenated using the + operator. This operation combines two or more tuples to create a new tuple.
Note: Only tuples can be concatenated with tuples. Combining a tuple with other types like lists will raise an error. Tuples themselves can contain mixed datatypes."""

tup1 = (0, 1, 2, 3)
tup2 = ('Geeks', 'For', 'Geeks')
tup3 = tup1 + tup2
print(tup3) # (0, 1, 2, 3, 'Geeks', 'For', 'Geeks')

"""Slicing of Tuple
Slicing a tuple means creating a new tuple from a subset of elements of the original tuple. The slicing syntax is tuple[start:stop:step].
Note: Negative Increment values can also be used to reverse the sequence of Tuples. """
 

tup = tuple('HELLO WORLD')
print(tup[::-1]) # ('D', 'L', 'R', 'O', 'W', ' ', 'O', 'L', 'L', 'E', 'H')
print(tup[::2]) # ('H', 'L', 'O', 'W', 'R', 'D') skip every second element
print(tup[-1::]) # ('d',) will print only last element

"""Deleting a Tuple
Since tuples are immutable, we cannot delete individual elements of a tuple. However, we can delete an entire tuple using del statement.
Note: Printing of Tuple after deletion results in an Error. """
tup = (0, 1, 2, 3, 4)
del tup
print(tup)

# ERROR!
# Traceback (most recent call last):
# File "<main.py>", line 6, in <module>
# NameError: name 'tup' is not defined

'''Tuple Unpacking with Asterisk (*)
*operator is used in tuple unpacking to grab multiple items into a list. This is useful to extract just a few specific elements and collect the rest together.
Explanation: a gets the first item, c gets the last item and *b collects everything in between into a list.'''

tup = (1, 2, 3, 4, 5)
a, *b, c = tup
print(a) 
print(b) 
print(c)

# 1
# [2, 3, 4]
# 5



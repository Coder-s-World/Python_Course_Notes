"""Dictionary
Dictionary is a data structure that stores information in key-value pairs. While keys must be unique and immutable (like strings or numbers), values can be of any data type, whether mutable or immutable. This makes dictionaries ideal for accessing data by a specific name rather than a numeric position like in list.
A dictionary in Python is a collection of key–value pairs, where each key is unique and maps to a value.
🔹 Definition
A dictionary:
•	Stores data as key : value 
•	Keys must be unique 
•	Values can be anything (list, number, string, etc.) 
•	It is mutable (you can change it)
Here are the dictionary key rules in one line each 👇
•	Keys must be unique (no duplicates) 
•	Keys must be immutable (int, str, tuple allowed; list not allowed) 
•	Keys are case-sensitive ("a" ≠ "A") 
•	Keys must be hashable 
•	Keys can be of different data types 
•	In dict() syntax, keys must be valid identifiers (strings only) 
🔹 Important Concept
•	{} → flexible (any immutable key) ✅ 
•	dict() → only string keys (identifier style) ✅
•	d = dict(1="one")   # ❌ Error
•	❌ Because 1 is not a valid identifier"""



# Creating a Dictionary
# A dictionary is created by writing key-value pairs inside { }, where each key is connected to a value using colon (:). A dictionary can also be created using dict() function.
a = {1: 'hi', 2: 'For', 3: 'bye'}
print(a) # {1: 'hi', 2: 'For', 3: 'bye'}

b = dict(a = "hi", b = "for", c = "bye")
print(b) # {1: 'hi', 2: 'For', 3: 'bye'}


# Accessing Dictionary Items
# A value in a dictionary is accessed by using its key. This can be done either with square brackets [ ] or with the get() method. Both return the value linked to the given key.
# Access using key
print(d["name"]) # kat

# Access using get()
print(d.get("name")) # kat

""" Note: Accessing a missing key with [ ] raises a KeyError, while get() is safer because it returns None (or a default value) instead of an error."""

# Adding and Updating Dictionary Items
# New items are added to a dictionary using the assignment operator (=) by giving a new key a value. If an existing key is used with the assignment operator, its value is updated with the new one.
d = {1: 'hello', 2: 'For', 3: 'bye'}

# Adding a new key-value pair
d["age"] = 22

# Updating an existing value
d[1] = "Python dict"
print(d) # {1: 'Python dict', 2: 'For', 3: 'bye', 'age': 22}





'''Removing Dictionary Items
   Dictionary items can be removed using built-in deletion methods that work on keys:
•	del: removes an item using its key
•	pop(): removes the item with the given key and returns its value
•	clear(): removes all items from the dictionary
•	popitem(): removes and returns the last inserted key-value pair
d = {1: 'python', 2: 'java', 3: 'cyber', 'age':22}'''

# Using del 
del d["age"]
print(d) # {1: 'python', 2: 'java', 3: 'cyber'}

# Using pop() 
val = d.pop(1)
print(val) # python

# Using popitem()
key, val = d.popitem()
print(f"Key: {key}, Value: {val}") # Key: 3, Value: cyber

# Using clear()
d.clear()
print(d) # {}


'''Iterating Through a Dictionary
A dictionary can be traversed using a for loop to access its keys, values or both key-value pairs by using the built-in methods keys(), values() and items().'''

d = {1: 'while', 2: 'For', 'age':22}

# Iterate over keys
for key in d:
    print(key)
    
# 1
# 2
# age    

# Iterate over values
for value in d.values():
    print(value)

#while
# For
# 22

# Iterate over key-value pairs
for key, value in d.items():
    print(f"{key}: {value}")
    
# 1: while
# 2: For
# age: 22


'''Nested Dictionaries
A nested dictionary is a dictionary that contains another dictionary as one of its values. Below diagram shows how a nested dictionary works, where key 3 points to another dictionary inside the main dictionary.'''
 
d = {1: 'Geeks', 2: 'For', 3: {'A': 'Welcome', 'B': 'To', 'C': 'Geeks'}}
print(d)

'''Dictionary Comprehension
Dictionary comprehension is used to create a dictionary in a short and clear way. It allows keys and values to be generated from a loop in one line. This helps in building dictionaries directly without writing multiple statements.
Syntax
{key: value for (key, value) in iterable if condition}

•	key: The item to use as the dictionary key.
•	value: The item to use as the dictionary value.
•	iterable: Any sequence or collection to loop through.
•	condition (optional): Lets you include only certain items
•	sq = {x: x**2 for x in range(1, 6)}
•	print(sq) # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
•	
•	Explanation:
•	
•	x takes values from 1 to 5 and x becomes the key
•	x**2 becomes the value
•   Each key and value pair is added to the dictionary in one line'''


# Creating a Dictionary from Two Lists
# This method creates a dictionary by pairing each item from one list with the matching item from another list using zip().
# keys = ['a','b','c','d','e']
# values = [1, 2, 3, 4, 5]  

d = {k:v for (k,v) in zip(keys, values)}  
print (d)
# {'a': 1, 'c': 3, 'b': 2, 'e': 5, 'd': 4}

# Using fromkeys() Method
# The fromkeys() method creates a dictionary by taking a group of keys and assigning the same value to all of them.

d = dict.fromkeys(range(5), True)
print(d) # {0: True, 1: True, 2: True, 3: True, 4: True}

#Examples
# Example 1: This example demonstrates creating a dictionary by transforming and repeating characters from a string.

b = {x.upper(): x*3 for x in 'coding'}
print(b)
# Output - {'C': 'ccc', 'O': 'ooo', 'D': 'ddd', 'I': 'iii', 'N': 'nnn', 'G': 'ggg'}

# Example 2: This example maps a list of fruits to their name lengths

c = {fruit: len(fruit) for fruit in ['apple', 'banana', 'cherry']}
print(c)
 # Output - {'apple': 5, 'banana': 6, 'cherry': 6}

# Dictionary Comprehension with Conditional Statements
# We can include conditions in a dictionary comprehension to filter items or apply logic only to specific values. This allows us to create dictionaries more selectively.
d = {x: x**3 for x in range(10) if x**3 % 4 == 0}
print(d) # {0: 0, 8: 512, 2: 8, 4: 64, 6: 216}

# Nested Dictionary Comprehension
# We can also create dictionaries within dictionaries using nested dictionary comprehensions. This is useful when each key maps to another dictionary of related values.
d = {x: x**3 for x in range(10) if x**3 % 4 == 0}
print(d) # {0: 0, 8: 512, 2: 8, 4: 64, 6: 216}



"""Set
A Set in Python is used to store a collection of items with the following properties.
•	No duplicate elements. If try to insert the same item again, it overwrites previous one.
•	An unordered collection. When we access all items, they are accessed without any specific order and we cannot access items using indexes as we do in lists.
•	Internally use hashing that makes set efficient for search, insert and delete operations. It gives a major advantage over a list for problems with these operations.
•	Mutable, meaning we can add or remove elements after their creation, the individual elements within the set cannot be changed directly.
A set in Python is a collection of unique (no duplicates) and unordered elements.
________________________________________
🔹 Definition
A set:
•	Stores multiple items 
•	Does NOT allow duplicate values 
•	Is unordered (no indexing like list/tuple)
🔹 Key Properties
•	❌ No duplicates 
•	❌ No indexing (my_set[0] ❌) 
•	❌ No order guarantee 
•	✅ Mutable (you can add/remove items)
Create a Set"""
# 1. Using curly braces: s = {10, 20, 30}
# 2.Using set() function: s = set([1, 2, 2, 3])




"""Type Casting
set() method in python is used to convert other data types, such as lists or tuples, into sets."""

# typecasting list to set
s = set(["a", "b", "c"])
print(s)

# Adding Element 
# Adding element to the set
s.add("d")
print(s)

# Check unique and Immutable
"""Python sets cannot have duplicate values. While you cannot modify the individual elements directly, you can still add or remove elements from the set."""

# a set cannot have duplicate values
s = {"hi", "bye", "hi"}
print(s)

# values of a set cannot be changed
s[1] = "Hello"
print(s) # TypeError: 'set' object does not support item assignment

"""Frozen Sets
A frozenset is an immutable version of a set. Its elements cannot be changed after creation, but you can perform operations like union, intersection and difference. Use frozenset() to create one.
Note: Frozensets are immutable, so methods like add() or remove() cannot be used. They are also hashable, which allows them to be used as dictionary keys."""

 # Frozen set (immutable)
fs = frozenset(["e", "f", "g"])
print("Frozen Set:", fs) # ('Frozen Set:', frozenset(['e', 'g', 'f']))



"""Methods for Sets
1. Adding elements to Sets: add() function is used to insert new elements into a set. It automatically ignores duplicates."""

#adding element to set
s = {"a", "b", "c"}
s.add("d")
print(s) # {'c', 'd', 'a', 'b'}

"""2. Union of Sets: union() function combines two sets and returns a new set with all unique elements."""
# Union of Sets
a = {"x", "y"}
b = {"y", "z"}
u = a.union(b)
print(u) # {'z', 'y', 'x'}

"""3. Intersection of Sets: intersection() function returns a new set containing elements that are common to both sets."""
# Intersection of Sets
a = {1, 2, 3}
b = {2, 3, 4}
i = a.intersection(b)
print(i) # {2, 3}

"""4. Difference of Sets: difference() function returns a set containing elements that are in the first set but not in the second."""
# Difference of Sets
a = {1, 2, 3}
b = {2, 3, 4}
d = a.difference(b)
print(d) # {1}

"""5. Clearing a Set: clear() function removes all elements from a set, leaving it empty."""
#clearing a set
s = {1, 2, 3}
s.clear()
print(s) # set()


"""Operators for Sets"""
# Define two sets
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

# 1. Union (|) → all unique elements from both sets
print(a | b)        # {1, 2, 3, 4, 5, 6}

# 2. Intersection (&) → common elements
print(a & b)        # {3, 4}

# 3. Difference (-) → elements in 'a' but not in 'b'
print(a - b)        # {1, 2}

# 4. Difference (-) → elements in 'b' but not in 'a'
print(b - a)        # {5, 6}

# 5. Symmetric Difference (^) → elements in either set but NOT both
print(a ^ b)        # {1, 2, 5, 6}

# 6. Membership (in / not in) → check if element exists
print(2 in a)       # True (2 is in set a)
print(10 not in a)  # True (10 is not in set a)

# 7. Subset (<=) → all elements of first set are in second
x = {1, 2}
y = {1, 2, 3}
print(x <= y)       # True (x is subset of y)

# 8. Proper Subset (<) → subset but not equal
print(x < y)        # True

# 9. Superset (>=) → contains all elements of another set
print(y >= x)       # True (y is superset of x)

# 10. Proper Superset (>) → superset but not equal
print(y > x)        # True

# 11. Equality (==) → both sets have same elements
print({1, 2} == {2, 1})  # True

# 12. Inequality (!=) → sets are not equal
print(a != b)       # True


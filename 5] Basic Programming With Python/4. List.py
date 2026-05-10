List
List is built in data type which is use to store the elements. It is capable of storing multiple type data. 
In Python, a list is like a special container or a row of boxes where you can store a collection of items. These items can be numbers, words, or even a mix of different things all together. Imagine a list as a row of mailboxes, each with its own number starting from zero. You can put anything inside these mailboxes, and you can easily find or change what's inside by knowing the mailbox number.
-	List is mutable
-	It contain duplicate elements
-	It is heterogeneous means can hold multiple type of data like integer, string, Boolean, even other list and data type
-	It is maintain the order in which they are inserted
-	Elements can be accessed using index number which start from 0.
Creating list 
There are many ways to create list
1.	Using square brackets -  Square brackets [] are used to create a list directly.

a = [1, 2, 3, 4, 5] # List of integers
b = ['apple', 'banana', 'cherry'] # List of strings
c = [1, 'hello', 3.14, True] # Mixed data types
print(a)
print(b)
print(c)

2.	List() constructor - A list can also be created by passing an iterable (such as tuple, string or another list) to the list() constructor.

a = list((1, 2, 3, 'apple', 4.5))  
print(a)
b = list("GFG")
print(b)

3.	Creating List with Repeated Elements - A list with repeated elements can be created using the multiplication (*) operator.

a = [2] * 5
b = [0] * 7
print(a)
print(b)

Internal Representation of Lists
Python list stores references to objects, not the actual values directly.
•	The list keeps memory addresses of objects like integers, strings, or booleans.
•	Actual objects exist separately in memory.
•	Modifying a mutable object inside a list changes the original object.
•	Reassigning an immutable object creates a new object instead of changing the old one.
Accessing List elements
In Python, there are several common ways to access elements of a list. Here are the main ones, explained clearly:
________________________________________
1. Using Index (Single Element)
Lists are 0-indexed (first element is at index 0).
my_list = [10, 20, 30, 40]

print(my_list[0])  # 10
print(my_list[2])  # 30
________________________________________
2. Negative Indexing
Access elements from the end:
print(my_list[-1])  # 40 (last element)
print(my_list[-2])  # 30
________________________________________

3. Slicing (Multiple Elements)
Get a range of elements:
print(my_list[1:3])   # [20, 30]
print(my_list[:2])    # [10, 20]
print(my_list[2:])    # [30, 40]
________________________________________
4. Using Step in Slicing
Skip elements:
print(my_list[::2])   # [10, 30]
print(my_list[::-1])  # [40, 30, 20, 10] (reverse list)

Basic idea of slicing
Syntax:
list[start : end : step]
•	start → where to begin (default = start of list) 
•	end → where to stop (default = end of list) 
•	step → how many steps to jump
🔑 Simple way to remember:
•	::2 → skip 1, take 1 
•	[::-1] → reverse the list
•	+ step → move forward 
•	step → move backward 
•	2 → skip one element 
•	1 → take every element


________________________________________
5. Using Loop
Access elements one by one:
for item in my_list:
    print(item)
________________________________________
6. Using Index with Loop
If you need both index and value:
for i in range(len(my_list)):
    print(i, my_list[i])
OR (better way):
for i, val in enumerate(my_list):
    print(i, val)
________________________________________
7. Access Nested Lists
If list contains another list:
nested = [[1, 2], [3, 4]]
print(nested[0][1])  # 2


c=[5,6,8,9]
b=["hi",4.5,["cmdklcdmc"]]
a=list(("njkndkndn"))


print("0 index value is  ",c[0])
print("all values", c)
print("last value",c[-1])
print("o to last ", c[:4])
print("0 to all " , c[0:])
print("start with 1 and skip 1 values print ", c[1::2])

# start index value is 1, not mentioned end index value , skip value is -1 which print in reverse
print("print in reverse mode ",c[::-1])

Adding Elements into List
Elements can be added to a list using the following methods:
•	append(): Adds an single  element at the end of the list.  
Syntax of append() method
list.append(element)
Parameter:
element: The item to be appended to the list. This can be of any data type (integer, string, list, object, etc.). This parameter is mandatory, and omitting it will cause an error.

# append
# single element
a = [1,2,3]
a.append(4) 
print("after append 4 in list",a) # [1,2,3,4]

a.append([5,6])
print("after adding list to a",a) #[1,2,3,4,[5,6]]

for i in range(7,10):
    a.append(i)
print(a) # [1,2,3,4,[5,6],8,9]

extend(): extend() method is used to add items from one list to the end of another list. This method modifies the original list by appending all items from the given iterable. Using extend() method is easy and efficient way to merge two lists or add multiple elements at once. The extend() method can work with various types of iterables such as: Lists, Tuples, Sets and Strings (each character will be added separately) 


#extend - list_name.extend(iterable)
a = [1,2,3]
b = [5,8,"ghi"]

a.extend(b)
print(a)
print(b) # [1,2,3,5,8,'ghi']

# Using a tuple
a = [1, 2, 3]
b = (4, 5)
a.extend(b)
print(a) # [1,2,3,4,5]

# Using a set
a = [1, 2, 3]
b = {4, 5}
a.extend(b)
print(a)  # [1,2,3,4,5]

# Using a string
a = ['a', 'b']
b = "cd"
a.extend(b)
print(a) # [a,b,c,d] 

insert(): Adds an element at a specific position.
List insert() Method Syntax
list_name.insert(index, element)
Parameters:
index: the index at which the element has to be inserted.
element: the element to be inserted in the list.
Return : The insert() method returns None. It only updates the current list.


#insert - list_name.insert(index,element)
# Return : The insert() method returns None. It only updates the current list.

# 1. Inserting an Element to a specific index into the List
a = [5,6,8,9]
a.insert(0,4)
print(a) # Output-  [1, 2, 3, 4, 10, 5, 6, 7]


# Insertion in a List Before any Element
a = [5,6,8,9]
element = 4
before_Element = 8
index = a.index(before_Element)
a.insert(index,element)
print("before element " ,a) # [5,6,4,8,9]

# Inserting a Tuple into the List
a = [5,6,8,9]
b = ("nknk","kgjkg")
a.insert(2,b)
print("tuple with list", a)

# Inserting an Element at the end of the List
a = [5,6,8,9]
a.append(10)
print(a)

# Inserting a dictionary to a list in Python
my_list = [{'name': 'Alice', 'age': 30}, 
           {'name': 'Bob', 'age': 25}]
new_dict = {'name': 'Charlie', 'age': 40}
my_list.append(new_dict)
print(my_list)

# Python Insert List in Another List
d = [5,6,8,9]
e = ["nknk","kgjkg"]
d.append(e) 
d.insert(1,e)
d.extend(e)
print("append",d)
print("insert",d)
print("extend",d)


# Python Insert List in Another List
d = [5,6,8,9]
e = ["nknk","kgjkg"]
sum = d + e

•	clear(): removes all items. clear() method in Python is used to remove all elements from a list, effectively making it an empty list. This method does not delete the list itself but clears its content. It is a simple and efficient way to reset a list without reassigning it to a new empty list.
Syntax of clear() Method
list.clear()
Parameters:
The clear() method does not take any parameters.
Return Type:
It modifies the original list and does not return any value (None).

#Clearing a list of strings

# Clear all elements from the list 'a'
a = ["Geeks", "for", "Geeks"]
a.clear()
print(a) # output - []

Practical Applications of clear() Method
1. Reusing a List:
clear() method allows us to empty a list without creating a new one, making it easy to reuse the same list for storing new data.
2. Memory Optimization:
Using clear() helps in releasing the memory held by the elements of the list, making it available for other operations without creating a new list object.

Updating Elements into List

# Updating Elements into List
# Since lists are mutable, elements can be updated by assigning new values using their index.

a = [10, 20, 30, 40, 50]
a[1] = 25 
print(a)

# Output - [10, 25, 30, 40, 50]


Removing Elements from List
Elements can be removed from a list using the following methods:
•	remove(): Removes the first occurrence of an element.
•	pop(): Removes the element at a specific index or the last element if no index is specified.
•	del statement: Deletes an element at a specified index.

#remove()
list1 = [5,6,8,9,10]
list1.remove(5)
print("remove function", list1) # [5,8,9,10]

#pop 
list2 = [15,66,68,99,150]
list4 = [44,55,66]
list2.pop(0)
list4.pop()
print("pop with index",list2) # [66,68,99,150]
print("pop without index",list4) # [44,55]

# del
list3 = ['a','b','c','d']
del list3[2]
print(list3) # ['a','b','d']

# iterale over lists
a = ['apple', 'banana', 'cherry']
for item in a:
    print(item)
    # apple
    # banana
    # cherry

# Nested list - it is commonly used to represent matrices or tabular data. Nested elements can be accessed by chaining mul8,tiple indexes.

matrix = [[1,2,3],
          [4,5,6]
          [7,8,9]]
print(matrix[1][2])

List Comprehension in Python
List comprehension is a concise way to create new lists by applying an expression to each item in an existing iterable (like a list, tuple or range). It helps you write clean, readable and efficient code compared to traditional loops.
Syntax
[expression for item in iterable if condition]
Parameters:
•	expression: operation or value to include in the new list.
•	item: current element from the iterable.
•	iterable: sequence like a list, tuple or range.
•	if condition (optional): filter to include only items that satisfy the condition.
Why Use List Comprehension?
•	Cleaner code: Combines looping, filtering and transformation in one line.
•	More readable: Avoids verbose loops and temporary variables.
•	Faster execution: Often faster than equivalent for-loops.
•	# List Comprehension in Python
•	# Suppose you want to square every number in a list:
•	
•	list = [1,2,3,4,5]
•	square_list = [i ** 2 for i in list]
•	print(square_list) # [1, 4, 9, 16, 25]
•	
•	# # Suppose you want to mupltiply every number in a list:
•	list1 = [1,2,3,4,5]
•	mupltiply = [i * 2 for i in list1]
•	print(mupltiply) # [2, 4, 6, 8, 10]
•	
•	#Conditional Statements in List Comprehension
•	'''List comprehensions can use conditions to select or trans form items 
•	   based on specific rules. This allows creating customized lists 
•	   more concisely and improves code readability and efficiency.
•	
•	   This code uses a list comprehension with a condition 
•	   to create a new list containing only even numbers from the 
•	   original list a'''
•	
•	list2 = [1,2,3,4,5]
•	res = [i for i in list2  if i % 2 == 0]
•	print(res) # [2, 4]
•	
•	# Creating a list from a range
•	empt_list = [ val for val in range(30) if val % 3 == 0 ]
•	print(empt_list) # [0, 3, 6, 9, 12, 15, 18, 21, 24, 27]
•	
•	# Using nested loops: A list of all coordinate pairs in a 3x3 grid can be generated by combining two loops inside a list comprehension. This example produces every possible (x, y) pair where both x and y range from 0 to 2.
•	c = [(x, y) for x in range(3) for y in range(3)]
•	print(c) # [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]
•	
•	# Flattening a list of lists: A nested list (matrix) can be transformed into a single flat list by iterating through each sublist and its elements. This example flattens a 3x3 matrix into one continuous list of values.
•	mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
•	res = [val for row in mat for val in row]
•	print(res) # [1, 2, 3, 4, 5, 6, 7, 8, 9]
•	
•	#Explanation:
•	
•	'''mat is a list of lists (a 3x3 matrix).
•	[val for row in mat for val in row] goes through each sublist (row) and then each value (val) inside it.
•	It collects all values into a single flat list.'''




# LETS REVISE PYTHON
# LETS START WITH I/O OPERATIONS

# # TO TAKE AN INPUT FROM A USER WE USE THE INPUT FUNCTION
# name = input("Enter your name: ")
# age = input("Enter your age: ")

# # TO PRINT THE OUTPUT WE USE THE PRINT FUNCTION
# # AND WE CAN USE SPECIAL ARGUMENTS WHICH IS "SEP" TO SEPARATE THE OUTPUTS
# print("Hello", name, "you are", age, "years old", sep=" ", end=" :)")

# LETS MOVE TO THE CONTAINERS
# WE HAVE 4 TYPES OF CONTAINERS
# 1. LIST
# 2. TUPLE
# 3. SET
# 4. DICTIONARY

# LIST
# LIST IS A MUTABLE CONTAINER
# LIST IS A SEQUENCE OF ITEMS
# LIST IS A COLLECTION OF ITEMS
# LIST IS A COLLECTION OF HOMOGENEOUS OR HETEROGENEOUS ITEMS
# LIST IS A COLLECTION OF ITEMS WHICH ARE ORDERED
# LIST IS A COLLECTION OF ITEMS WHICH ARE INDEXED
# LIST IS A COLLECTION OF ITEMS WHICH ARE MUTABLE
# LIST IS A COLLECTION OF ITEMS WHICH ARE ITERABLE
# LIST IS A COLLECTION OF ITEMS WHICH ARE DYNAMIC
# LIST IS A COLLECTION OF ITEMS WHICH ARE GROWABLE
# LIST IS A COLLECTION OF ITEMS WHICH ARE HETEROGENEOUS
# LIST IS A COLLECTION OF ITEMS WHICH ARE DYNAMICALLY TYPED
list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# TO ACCESS IT FROM THE INDEX 0 TO 4 WE USE THE SLICING OPERATOR
print(list[:5])  # we don't specify the beginning index so it will start from 0

# TO ACCESS IT FROM THE INDEX 5 TO 9 WE USE THE SLICING OPERATOR
# we don't specify the ending index so it will end at the last index
print(list[5:])

# TO ACCESS CERTAIN RANGE WE SPECIFY THE BEGINNING AND ENDING INDEX
# it will start from index 2 and end at index 6, 7 is excluded and 2 is included
print(list[2:7])


# TO ACCESS THE LAST ELEMENT WE USE THE NEGATIVE INDEXING
print(list[-1])

# we can use the concept of slicing with negative indexing
print(list[-3:])  # it will print the last 3 elements

# we can specify the step of slicing
# it will print the elements from index 2 to 8 with a step of 2
print(list[2:8:2])  # still last element is excluded


# Tuple
# Tuple is a immutable container
# Tuple is a sequence of items
# Tuple is a collection of items
# Tuple is a collection of homogeneous or heterogeneous items
# Tuple is a collection of items which are ordered
# Tuple is a collection of items which are indexed
# Tuple is a collection of items which are iterable
# Tuple is defined by ()
tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(tuple[4])  # we can access the elements of tuple using indexing
print(tuple[-3:])
print(tuple[:])  # this imply all rows and all columns


# we use tuples if we have some informations that are not going to change
# so it will be more efficient to use tuples instead of lists
# because tuples are set into the memory as one chunk of data.

# 3. SET
# Set is a collection of items
# Set is a collection of items which are unordered
# Set is a collection of items which are unindexed
# Set is a collection of items which are iterable
# Set is a collection of items which are mutable
# Set is a collection of items which are heterogeneous
# Set is a collection of items which are dynamically typed
# Set is a collection of items which are unique
# Sets is defined by {}
# when printing it, it will print only unique elements
set = {1, 2, 3, 1, 2, 3}
print(set)


# 4. DICTIONARY
# Dictionary is a collection of items
# Dictionary is a collection of items which are unordered
# Dictionary is a collection of items which are unindexed
# Dictionary is a collection of items which are iterable
# Dictionary is a collection of items which are mutable
# Dictionary is a collection of items which are heterogeneous
# Dictionary is a collection of items which are dynamically typed
# Dictionary is a collection of items which are unique
# Dictionary is a collection of items which are key-value pairs
# Dictionary is defined by {}
# when printing it, it will print only unique elements
dictionary = {"name": "John", "age": 20}
# we can access the elements of dictionary using keys
print(dictionary["name"])


# NOTE THAT ALL VARIABLES IN PYTHON ARE PASSED BY REFERENCE
# SO IF WE CHANGE THE VALUE OF A VARIABLE IN A FUNCTION
# IT WILL CHANGE THE VALUE OF THE VARIABLE IN THE MAIN PROGRAM


# is operator is used to check if two variables are pointing to the same object
# == operator is used to check if two variables have the same value
X = [3, 4, 5]
Y = [3, 4, 5]
Z = X
print(X == Y)  # True, BECAUSE BOTH HAVE THE SAME VALUES
print(X is Y)  # False BECAUSE THEY ARE NOT POINTING TO THE SAME OBJECT
print(X is Z)  # True BECAUSE THEY ARE POINTING TO THE SAME OBJECT
print(X == Z)  # True BECAUSE THEY HAVE THE SAME VALUES


# we can make a list from 1 to 10 in one line
list = [i for i in range(1, 11)]
print(list)

# to cast an integer into char we use chr function
print(chr(65))  # it will print A


#########################################################################################################
# Lets start python now,
# we use python libraries to make our life easier
# so the first library you must know is math library -> numpy
# numpy is a library for scientific computing
# it is used for linear algebra, fourier transform, and matrices
# it is used for multidimensional arrays
# it is used for mathematical operations on arrays
# it is used for fast operations, because it is written in C, and very optimized
# it is used for random number generation
# so whenever you are going to use matricies or vectors, you must use numpy

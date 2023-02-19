"""
Numeric Data Types
"""

print("Python has three numeric types: int, float, and complex")    # print title 

#int data type
myValue=1                                                           # sets myValue as a variable with 1
print(myValue)                                                      # prints myValue variable    
print(type(myValue))                                                # prints myValue object type, gets data type of the variable and prints the class of the variable
print(str(myValue) + " is of the data type " + str(type(myValue)))  # print uses str() function to combine numbers and text, which converts an argument into a collection of letters called a string.
""" Integer
int (signed integers) 
They are often called just integers or ints. They are positive or negative whole numbers with no decimal point. 
Integers in Python 3 are of unlimited size. Python 2 has two integer types - int and long.
"""

# Float data type
myValue=3.14                                                        # sets myValue as a variable with 3.14
print(myValue)                                                      # prints myValue variable 
print(type(myValue))                                                # prints myValue object type, gets data type of the variable and prints the class of the variable
print(str(myValue) + " is of the data type " + str(type(myValue)))  # print uses str() function to combine numbers and text into string.
""" Float 
A float is a type of value in Python. When called, float() returns a floating point number or a decimal point
 for a provided number or string. Float values in Python are represented as 64-bit double-precision values. 
 1.8 x 10308 is the maximum value for any floating-point number.
"""

#Complex data type
myValue=5j                                                          # sets myValue as a variable with 5j
print(myValue)                                                      # prints myValue variable 
print(type(myValue))                                                # prints myValue object type, gets data type of the variable and prints the class of the variable
print(str(myValue) + " is of the data type " + str(type(myValue)))  # print uses str() function to combine numbers and text into string.
""" Complex
The complex data type in python consists of two values, the first one is the real part of the complex number, 
and the second one is the imaginary part of the complex number. We usually denote the real part using i and the 
imaginary part with j. For example, (3 + 7j) or (3i + 7j).
"""

#Bool data type
myValue=True                                                        # sets myValue as a variable with True
print(myValue)                                                      # prints myValue variable
print(type(myValue))                                                # prints myValue object type, gets data type of the variable and prints the class of the variable
print(str(myValue) + " is of the data type " + str(type(myValue)))  # print uses str() function to combine numbers and text into string.

myValue=False                                                       # sets myValue as a variable with False
print(myValue)                                                      # prints myValue variable
print(type(myValue))                                                # prints myValue object type, gets data type of the variable and prints the class of the variable
print(str(myValue) + " is of the data type " + str(type(myValue)))  # print uses str() function to combine numbers and text into string.
""" Boolean
The Python Boolean type is one of Python's built-in data types. It's used to represent the truth value of an expression. 
For example, the expression 1 <= 2 is True, while the expression 0 == 1 is False . 
Understanding how Python Boolean values behave is important to programming well in Python.
"""

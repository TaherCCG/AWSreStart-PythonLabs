"""
String Data Types
"""

print("Python String Data Type")                                    # print title 

myString = "This is a string."                                      # defines a myString as variable with string data              
print(myString)                                                     # prints myString variable
print(type(myString))                                               # prints myString variable object type, gets data type of the variable and prints the class of the variable 
print(myString + " is of the data type " + str(type(myString)))     # prints myString variable + string + string object type for myString variable. 

firstString = "water"                                               # defines a firstString as variable with string data
secondString = "fall"                                               # defines a secondString as variable with string data
thirdString = firstString + secondString                            # defines a thirdString as variable with string data of firstString plus secondString
print(thirdString)                                                  # print thirdString

name = input("What is your name? ")                                 # defines name as variable which asks the user to input name
print(name)                                                         # print name variable

color = input("What is your favorite color?  ")                     # defines color as variable which asks the user to input color   
animal = input("What is your favorite animal?  ")                   # defines animal as variable which asks the user to input animal
print("{}, you like a {} {}!".format(name,color,animal))            # print formatted message with 3 variables

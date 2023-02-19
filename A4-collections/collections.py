print("Python List[] Tuple() and Dictionary{} \n")          # print Title


""" Defining a list 
To create a list in Python, we use square brackets ( [] ). 
Here's what a list looks like: ListName = [ListItem, ListItem1, ListItem2, ListItem3, ...] 
Note that lists can have/store different data types.
"""
myFruitList = ["apple", "banana", "cherry"]                 # defines myFruitList as list variable containing data 
print(myFruitList)                                          # print list variable (myFruitList)
print(type(myFruitList))                                    # print variable object type for myFruitList variable


""" Accessing a list by position """

print(myFruitList[0])                                       # print the list value at position 0
print(myFruitList[1])                                       # print the list value at position 1
print(myFruitList[2])                                       # print the list value at position 2

""" Changing the values in a list """

myFruitList[2] = "orange"                                   # defines myFruitList value at position 2 to "orange"   
print(myFruitList)                                          # print myFruitList


""" Defining a tuple
Tuples can be defined using any variable name and then assigning different values 
to the tuple inside the round brackets ( () ). The tuple is ordered, unchangeable, and allows duplicate values.
"""
myFinalAnswerTuple = ("apple", "banana", "pineapple")       # defines myFinalAnswerTuple as a tuple variable containing data 
print(myFinalAnswerTuple)                                   # prints variable
print(type(myFinalAnswerTuple))                             


""" Accessing a tuple by position """

print(myFinalAnswerTuple[0])                                # print the tuple value at position 0
print(myFinalAnswerTuple[1])                                # print the tuple value at position 1
print(myFinalAnswerTuple[2])                                # print the tuple value at position 2


""" Defining a dictionary 
A dictionary consists of a collection of key-value pairs. Each key-value pair maps the key to its associated value. 
You can define a dictionary by enclosing a comma-separated list of key-value pairs in curly braces ( {} ).
"""
myFavoriteFruitDictionary = {                               # defines myFavoriteFruitDictionary as a Dictionary variable containing data 
  "Akua" : "apple",                                         # data is stored as key : value
  "Saanvi" : "banana",                                      # each key:value is separated by comma   
  "Paulo" : "pineapple"
}


print(myFavoriteFruitDictionary)                            # prints variable
print(type(myFavoriteFruitDictionary))                      # print variable object type for myFavoriteFruitDictionary variable


""" Accessing a dictionary by name """

print(myFavoriteFruitDictionary["Akua"])                    # print the value of dictionary at key value "Akua"
print(myFavoriteFruitDictionary["Saanvi"])                  # print the value of dictionary at key value "Saanvi"
print(myFavoriteFruitDictionary["Paulo"])                   # print the value of dictionary at key value "Paulo"

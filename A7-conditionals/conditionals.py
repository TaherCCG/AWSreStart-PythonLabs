"""
Working with Conditionals

Lab overview
A section of code that compares two pieces of information is called a conditional statement. You can use conditionals to create different paths through the program. Using comparative operators, you will write a program that makes decisions.

Use the if statement
Use the else statement
Use the elif statement

"""

# Working with the if statement

userReply = input("Do you need to ship a package? (Enter yes or no) ")      # define variable userReply as input to ask user question. (this will set the variable value to userReply)
if userReply == "yes":                                                      # if variable is yes the print line below
    print("We can help you ship that package!")                             # print message    
# Working with the else statement
else:                                                                       # else print the line below  (if userReply variable is not "yes")
    print("Please come back when you need to ship a package. Thank you.")   # prints message 
   
# Working with the elif statement

userReply = input("Would you like to buy stamps, buy an envelope, or make a copy? (Enter stamps, envelope, or copy) ")  # define variable userReply as input to to set value for the variable
if userReply == "stamps":                                                   # if userReply is stamps print line below
    print("We have many stamp designs to choose from.")
elif userReply == "envelope":                                               # else if userReply is envelope print line below
    print("We have many envelope sizes to choose from.")
elif userReply == "copy":                                                   # else if userReply is copy then                    
    copies = input("How many copies would you like? (Enter a number) ")     # define var copies as input from user. (users input will be set as value for var)
    print("Here are {} copies.".format(copies))                             # print message with number of copies (using var copies) as formatted
else:                                                                       # else print line below
    print("Thank you, please come again.")                                  # if userReply was not stamps, envelope or copy then it will print this message
    

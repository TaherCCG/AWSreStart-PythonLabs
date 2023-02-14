"""
Working with Conditionals

Lab overview
A section of code that compares two pieces of information is called a conditional statement. You can use conditionals to create different paths through the program. Using comparative operators, you will write a program that makes decisions.

In this lab, you will:

Use the if statement
Use the else statement
Use the elif statement

"""

# Working with the if statement

userReply = input("Do you need to ship a package? (Enter yes or no) ")      #input ask user question. user reply yes/no
if userReply == "yes":                                                      # if yes the print line below
    print("We can help you ship that package!")        
# Working with the else statement
else:                                                                       # else print the line below  (if answer is no)
    print("Please come back when you need to ship a package. Thank you.")
   
# Working with the elif statement

userReply = input("Would you like to buy stamps, buy an envelope, or make a copy? (Enter stamps, envelope, or copy) ")  #ask user question. user reply stamps/envelope/copy
if userReply == "stamps":                                                   # if userReply is stamps print line below
    print("We have many stamp designs to choose from.")
elif userReply == "envelope":                                               # else if userReply is envelope print line below
    print("We have many envelope sizes to choose from.")
elif userReply == "copy":                                                   #else if userReply is copy then                    
    copies = input("How many copies would you like? (Enter a number) ")     # ask user how many copies. store input as copies
    print("Here are {} copies.".format(copies))                             # print number of copies
else:                                                                       # else print line below
    print("Thank you, please come again.")
    

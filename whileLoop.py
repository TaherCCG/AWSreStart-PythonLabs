"""
Working with Loops
"""
#Printing the game rules
print("Welcome to Guess the Number!")
print("The rules are simple. I will think of a number, and you will try to guess it.")


# Importing random and writing a while loop
import random
number = random.randint(1,10)                               # selects number between 1 and 10
isGuessRight = False                                        # if guess is false then it goes into while loop
while isGuessRight != True:                                 # whileLoop loops until the guess is true.   
    guess = input("Guess a number between 1 and 10: ")      # Asks user to input number
    if int(guess) == number:                                # check if guess is equal to number
        print("You guessed {}. That is correct! You win!".format(guess))  #tell the user it was the correct guess and exit the loop
        isGuessRight = True                                 # isGuessRight is true
    else:                                                   # else if the wrong guess then
        print("You guessed {}. Sorry, that isn’t it. Try again.".format(guess))   # tell the user it was the wrong guess and continue the loop.
        print("Count to 10!")


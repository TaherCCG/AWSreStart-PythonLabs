"""
Working with Loops
"""
#Printing the game rules
print("Welcome to Guess the Number!")
print("The rules are simple. I will think of a number, and you will try to guess it.")


# Importing random and writing a while loop
import random                                               # imports random module
number = random.randint(1,10)                               # defines var number to random integer between 1 and 10
isGuessRight = False                                        # defines var isGuessRight to False
while isGuessRight != True:                                 # while var isGuessRight is not True, it loops until the guess is true.   
    guess = input("Guess a number between 1 and 10: ")      # defines var guess to get value as input from user
    if int(guess) == number:                                # if var guess is equal to var number
        print("You guessed {}. That is correct! You win!".format(guess))  #prints to inform the user it was the correct guess as formatted
        isGuessRight = True                                 # var isGuessRight is True ends loop
    else:                                                   # else if guess was not true then
        print("You guessed {}. Sorry, that isn’t it. Try again.".format(guess))   # tell the user it was the wrong guess and continue the loop, as formatted
        print("Count to 10!")                               # prints message


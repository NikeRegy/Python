# First how to generate random numbers in python

import random
#print(help(random))

#number = random.randint(1, 8) #For a random whole integer. The bracket will hold your range (similar to rolling a dice. Everytime yuo run this program, it gives you a different random number)

# You can aslo use variables as your range i.e
low = 1
high = 100
number = random.randint(low, high)

#For a random float number, random.random() (For an empty bracket, it returns a random float between 0 & 1)
#number = random.random()

#You can also make a random choice from a sequence using the random.choice () function i.e given the tuple below; plus its also use for games
options = ("rock", "paper", "scissors")
option = random.choice(options)

# The random.shuffle() function is used to shuffle
cards = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A" ]
random.shuffle(cards)


#rint(cards)





# Exercis - Number Guessing Game

import random


lowest_num = 1
highest_num = 100
answer = random.randint(lowest_num, highest_num)
guesses = 0
is_running = True


print("Python Number Guessing Game")
print(f"Select a anumber between {lowest_num} and {highest_num}")

while is_running:

    guess = input("Enter your guess: ")

    if guess.isdigit():
        guess = int(guess)
        guesses += 1


        if guess < lowest_num or guess > highest_num:
            print("That number is out of range")
            print(f"Please select a number between {lowest_num} and {highest_num}")
        elif guess < answer:
            print("Too low! Try again!")
        elif guess > answer:
            print("Too high! Try again!")
        else:
            print(f"CORRECT! The answer was {answer}")
            print(f"Number of guesses: {guesses}")
            is_running = False




    else:
        print("Invalid guess")
        print(f"Please select a number between {lowest_num} and {highest_num}")

















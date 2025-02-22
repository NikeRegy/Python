# While loop = execute some code WHILE some condition remains true
# A while loop will contine to execute unless you give an escape command 


name = input("Enter your name: ")

while name == "":
    print("You did not enter your name")
    name=("Enter your name: ")
    
print(f"Hello {name}")

age = int(input("Enter your age: "))

while age < 0:
    print("Age cannot be negative")
    age = int(input("Enter your age: "))
print(f"You are {age} years old")
   


# Logical operators can be used in while loops as well

food = input("Enter a food you like (q to quit): ")

while not food == "q":
    print(f"You like {food}")
    food = input("Enter another food you like (q to quit): ")
print("bye")

num = int(input("Enter a # between 1 -10: "))

while num < 1 or num > 10:
    print(f"{num} is not valid!")
    num = int(input("Enter a # between 1 -10: "))
print(f"Your number is {num}")


# for loops = execute a block of code a fixed number of times.
# You can iterate over a range, string, sequence, etc
for x in reversed(range(1,11)):                 # the reversed function helps in counting backwards
    print(x)                                    # iteration works on string variables as well
print("Happy New Year")

credit_card = "3673-7584-6198-8721"
for x in credit_card:
    print(x)
    
for x in range(1, 20):          # to skip over an element in an iteration process, you can use the continue keyword
    if x == 13:                 # to exit the loop, use the break keyword 
        break
    else:
        print(x)






































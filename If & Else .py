# If is used to do some code IF some condition is true 
# Else is used to do something else 

age = int(input("Enter your age: "))

if age >= 18:
    print("You are now signed up!")
elif age < 0:
    print("You haven't been born yet")
elif age >= 100:
    print("You are too old to sign up") 
else:
    print("You must be 18 years old or older to sign up!")
    
# Use double equal sign for comparison
response = input("Would you like food? (Y/N): ")

if response == "Y":
    print("Have some food!")
else:
    print("No food for you!")
    

name = input("Enter your name: ")

if name == "":
    print("You did not type in your name!")
else:
    print(f"Hello {name}")
    
# Booleans can also be used with conditional statements

for_sale = True

if for_sale:
    print("This item is for sale")
else:
    print("This item is not for sale")
    
online = False
if online:
    print("I need to talk to you right now")
else:
    print("I'm leaving you a message")

# Booleans do not need inputs for the code to run
# With IF statements, youo either write a condition or make use of boolean

    
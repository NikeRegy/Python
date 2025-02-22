# function = A block of reusable code. place () after the funftion name to invoke it

def happy_birthday(name, age): 
    print(f"Happy birthday to {name}!")
    print(f"You are {age} years old!")
    print("Happy birthday! Happy birthday!")
    print("Happy birthday to you!")
    print()

happy_birthday("Rejoice", 17)
happy_birthday("Jerrick", 7)
happy_birthday("Grace", 12)
 
# Instead of rewriting this code based on the number of times you want it in the outcome, you can use functions to just recall it over and over again
# Always remember to add brackets at the end of any function name to call it
# You can add parameters to you function. Those parameters can be otherwise known as arguments
# The order in which you add this parameters maters alot.
# Diff between an argument and a parameter is that a parameter can be seen as a variable name while the argument is the element in that variable
# The position of your parameter matters alot as it goes hand in hand with the argument


def display_invoice(username, amount, due_date):
    print(f"Hello {username}")
    print(f"Your bill of ${amount:.2f} is due: {due_date}")

display_invoice("Asaph", 4000, "27th January, 2025")



# return = statement used to end a function and send a result back to the caller

def add(x, y):
    z = x + y
    return z

def subtract(x, y):
    z = x - y
    return z

def multiply(x, y):
    z = x * y
    return z

def divide(x, y):
    z = x / y
    return


print(add(1, 2))
print(subtract(1, 2))
print(multiply(1, 2))
print(divide(1, 2))





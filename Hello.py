print("hello world")     # Result will be: hello world
#This is my first python program
print("I like swallow")       # Result will be: I like swallow
print("Its really good!")       # Result will be: Its really good!


# Variable = A container for a value (string, integer, float, boolean). A variable behaves as if it was the value it contains

# Strings: Strings are characters in text format and should be in quotes ""
first_name = "Rejoice"
print(first_name)       # Result will be: Rejoice       
food = "Swallow"
email = "rejoice7@hull.com"

# f-string: formatted string; it enables you to embed expressions inside strings using curly brackets {} and they are only used when you want to insert a variable
print(f"Hello {first_name}")        # Result will be: Hello Rejoice
print(f"You like {food}")       # Result will be: You like swallow
print(f"Hello {first_name}, You like {food}")       # Result will be: Hello Rejoice, You like swallow
print(f"You can send me a message at {email}")      # Result will be: You can send me a message at rejoice7@hull.com
# Note: You can use more than one f-string at once

# Integers are whole numbers and should not be in quotes
age = 25
print(age)      # Result will be: 25
print(f"You are {age} years old")       # Result will be: You are 25 years old
quantity = 5
print(f"You are now the owner of {quantity} of these cars")     # Result will be: You are now the owner of 5 of these cars
num_of_students = 30
print(f"We have {num_of_students} students that will be volunteering for the event")        # Result will be: We have 30 students that will be volunteering for the event

# Float: Floating point number (has decimal points)
price = 20.09
print(price)        # Result will be: 20.09
print(f"The cost of fuel is now {price}")       # Result will be: The cost of fuel is now 20.09
print(f"The cost of fuel is now ${price}")      # Result will be: The cost of fuel is now $20.09
CGPA = 4.28
print(F"My CGPA is now {CGPA}")         # Result will be: My CGPA is now 4.28
distance = 6.3
print(f"You ran {distance}km")          # Result will be: You ran 6.3km

# Boolean: A boolean is a logical value (returning either true or false)
is_student = True
is_not_student = False
print(f"Are you a student? {is_student} Are you a student? {is_not_student}")      
for_sale = True
if for_sale:
    print("That item is for sale")      
else:
    print("That item is NOT for sale")



# Test: Write out examples of the 4 types of variables
# String:
nick_name = "Tabby"
# Integer:
age = 13
# Float:
weight = 32.7
# Boolean:
is_a_great_cook = False
print(f"She is {nick_name}. {nick_name} is {age} years old and weighs {weight}kg.")   # Result will be: She is Tabby. Tabby is 13 years old and weighs 32.7kg. 
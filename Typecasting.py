# Typecasting is the process of converting a variable from one type to another i.e str(), int(), float(), bool()
 
name = "Rejoice"
age = 17
gpa = 3.78
is_student = True

print(type(name))
print(type(age))
print(type(gpa))
print(type(is_student))

gpa = int(gpa)

print(gpa)

age = float(age)
print(age)
# Typecasting an integer to a string will only change the type from integer to string but not the value.
name = bool(name)
print(name)
# Typecasting a string to boolean will always give True as result, it willl only be false when it is null/empty
# TYpecasting is very useful with handling user input


# input() is a function that prompts a user to enter data and returns the data as a string

input("What is your name?: ")
name = input("What is your name:")
print(f"Hello {name}")

name =  input(("What is your name?:  "))
print(f"Hello there {name}!")

age = input("What is your age?: ")
print(f"I am {age} years old.")
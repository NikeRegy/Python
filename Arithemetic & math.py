'''friends = 0
# friends = friends + 1
friends += 1'''

# Note that += is an augumented form of writing 'friends = friends + 1'
# The same goes for any and all of the other arithemetic operators

'''friends = 5
friends += 5
# Addition
friends -= 3
# Subtraction
friends *= 2
# Multiplication
friends /= 2 
# Division
friends **= 2
# Exponent

remainder = friends % 4
# Modulus (%) the remainder operator 
print(remainder)'''


# x = 3.14
# y = 4
# z = 5

'''result = round(x)
print(result)'''
# The 'round' function rounds up a number to the nearest integer.

'''result = abs(y)
print(result)'''
# The absolute value function 'abs' returns the absolute value for any integer.

x = 3.14
y = 4
z = 5

'''result = pow(y, 3)
print(result)'''
# The power function 'pow' is an exponential function and its syntax is pow("The base", "The power")

'''result = max(x, y, z)
print(result)
result = min(x, y, z)
print(result)'''
# The 'max' and 'min' functions return the maximum and minimum values in a given set.

import math

x = 9.6
#print(math.pi)
#print(math.e)
#result = math.sqrt(x)
#result = math.ceil(x)
result = math.floor(x)

# The squareroot 'sqrt' function returns the squareroot of a particular value
# The ceil function rounds up a value to the next int i.e 9.6 will be rounded up to 10, but an intersting fact is that even a 9.3 will still be rounded up to a 10
# The floor function rounds down a value to the whole number part of the value i.e 9.6 will be rounded down to a 9

print(result)




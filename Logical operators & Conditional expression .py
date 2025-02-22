# Logical operators = evaluate multiple conditions (or, and, not)
# or = at least one condition must be True
# and = both conditions must be True
# not = inverts the condition (not False, not True)                        

#temp = -102
'''is_raining = False
if temp > 35 or temp < 0 or is_raining:
    print("The outdoor event is cancelled")
elif temp > 0 or temp < 35:
    print("The outdoor event has been rescheduled")
else:
    print("The outdoor event is still scheduled")'''
    
#is_sunny = True

'''if temp >= 28 and is_sunny:
    print("It is hot outside")
    print("It is SUNNY")
elif temp <= 0 and is_sunny:
    print("It is COLD outside")
    print("It is SUNNY")
elif temp < 28 and temp >0 and is_sunny:
    print("It is warm outside")
    print("It is SUNNY")''' 
    

'''if temp >=28 and is_sunny:
    print("It is hot outside")
    print("It is SUNNY")
elif temp <= 0 and is_sunny:
    print("It is COLD outside")
    print("It is SUNNY")
elif temp < 28 and temp >0 and is_sunny:
    print("It is warm outside")
    print("It is SUNNY")
elif temp >= 28 and not is_sunny:
    print("It is HOT outside")
    print("It is cloudy")
elif temp <= 0 and not is_sunny:
    print("It is cold outside")
    print("It is cloudy")
elif 28 > temp > 0 and not is_sunny:
    print("It is warm outside")
    print("It is cloudy")
else:
    print("Its a perfect weather")'''
    
'''temp = -102
is_sunny = False


if temp > 15 and is_sunny:
    print("It is WARM outside")
    print("It is SUNNY")
elif -15 > temp > 0 and not is_sunny:
    print("It is COLD outside")
    print("It is CLOUDY")
elif 15 > temp > 60 and is_sunny:
    print("It is HOT outside")
    print("It is SUNNY")
else:
    print("It is a perfect weather!")'''
    
    
# temp < 28 and temp > 0 can be wriiten as an inequality: 28> temp > 0

#Conditional expression = A one-line shortcut for the if-else statement
#                         Print or assign one of two values based on a condition
#                         X if condition else Y

#num = 16

#print("Positive" if num > 0 else "Negative")

'''result = "EVEN" if num % 2 == 0 else "ODD"
print(result)'''

'''a = 8
b = 9
#max_num = a if a > b else b
min_num = a if a < b else b
#print(max_num)
print(min_num)'''


'''age = 15
status = "Adult" if age >= 18 else "Child"

print(status)'''

'''temp = 17
weather = "HOT" if temp > 20 else "COLD"
print(weather)'''

user_role = "intern"
access_level = "Full Access" if user_role == "admin" else "Limited Access"
print(access_level)
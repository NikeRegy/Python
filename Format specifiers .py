# Format specifiers = {value:flags} format a value based on what flags are inserted


# .(number)f = round to that many decimal places (fixed point)
# :(number) = allocate that many spaces
# :03 = alllocate and zero pad that many spaces
# :< = left justify
# :> = right justify
# :^ = center align
# :+ = use a plus sign to indicate +ve value
# := = place sign to leftmost position
# :  = insert a space before positive numbers
# :, = comma separator
# Note that mixture of 2 or more flags is allowed based on what you are looking for or what you need to achieve


price1 = 3.14159
price2 = -987.65
price3 = 12.34

# reducing or increasing the decimal places (.(number)f) 
'''print(f"Price 1 is ${price1:.2f}")
print(f"Price 2 is ${price2:.2f}")
print(f"Price 3 is ${price3:.2f}")'''

# allocating a number of spaces
'''print(f"Price 1 is ${price1:10}")
print(f"Price 2 is ${price2:10}")
print(f"Price 3 is ${price3:10}")'''

# zero padding
'''print(f"Price 1 is ${price1:010}")
print(f"Price 2 is ${price2:010}")
print(f"Price 3 is ${price3:010}")'''

# left align
'''print(f"Price 1 is ${price1:<}")
print(f"Price 2 is ${price2:<}")
print(f"Price 3 is ${price3:<}")'''

# right align
'''print(f"Price 1 is ${price1:>10}")
print(f"Price 2 is ${price2:>10}")
print(f"Price 3 is ${price3:>10}")'''

# center align
'''print(f"Price 1 is ${price1:^10}")
print(f"Price 2 is ${price2:^10}")
print(f"Price 3 is ${price3:^10}")'''

# to display a plus sign to indicate +ve value. A space can also be used or even comma for thousand separation
'''print(f"Price 1 is ${price1:+}")
print(f"Price 2 is ${price2:+}")
print(f"Price 3 is ${price3:+}")'''

# to assign to the leftmost position
'''print(f"Price 1 is ${price1:=}")
print(f"Price 2 is ${price2:=}")
print(f"Price 3 is ${price3:=}")'''
















# dictionary = a collection of {key:value} pairs. A dictionary is ordered and changeable. No duplicates




capitals = {"USA": "Washington D.C",
            "India": "New Delhi",
            "China": "Beijing",
            "Russia": "Moscow"}

# To see attributes and methods of a dictionary,use the dir function; print(dir(capitals))
# For an indepth description, use the help function; print(help(capitals))

# To get a value from a dictionary, type the key; 
# print(capitals.get("China"))
# If python doesn't get the key, it will return the value "None". PS: It can be used within an if statement i.e

if capitals.get("Canada"):
    print("That capital exists")
else:
    print("That capital doesn't exist")

# To update (add to) a dictionary use the .update function. It can also be used to update an already existing key:value pair i.e
capitals.update({"Germany": "Berlin", "Nigeria": "Abuja"})
print(capitals)

# To remove values from a dictionary, use the .pop function. Also using the .popitem function, you don't have to pass in a key value, it pops the last key value pair in the dictionary
capitals.pop("China")
capitals.update({"Germany": "Berlin", "Nigerai": "Abuja"})
capitals.popitem()

# To completely erase a dictionary, use the .clear function
#capitals.clear()

# To get just the keys in a dictionary without their values, use .keys() and additionally, they can be used in loops (they are iterable)
keys = capitals.keys()
for key in capitals.keys():
    print(key)
                      

# To get just the values within your dictionary use the .values() funtion
values = capitals.values()
for value in capitals.values():
    print(value)

#When you use the .items() function, it returns  a 2D list of tuples
items = capitals.items()
for key, value in capitals.items():
    print(f"{key}: {value}")














#print(items)






















































































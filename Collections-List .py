# Collection = single "variable" used to store multiple values
# List = [] ordered and changeable. Duplicates OK
# Set = {} unordered and immutable, but Add/Remove OK. NO duplicates
# Tuples = () ordered and unchangeable. Duplicates OK. FASTER


# LISTS
fruits = ["apple", "orange", "banana", "coconut", "pineapple"]
for fruit in fruits:
    print(fruit)
print(fruits[::-1])

# Indexing can also be used to access the values in a list or a collection
# To list the different methods that can be used within a list, use the dir() function
print(dir(fruits))

# For a description for all these methods, use the help() function
print(help(fruits))
print(len(fruits))
print("apple" in fruits)
print("carrots" in fruits)
# Using the "in" function to see if an element is in the list or not always returns a boolean
# We can edit the elements in a list, using index

fruits[0] = "carrot" 
print(fruits)
for fruit in fruits:
    print(fruit)

#.append() is used to add elements to the end of a list
#.remove() is used to remove elements from a list
#.insert() is used to insert a value at a given index. It should have 2 arguments; the index you want to assign it to and then the value you want to insert 
#.sort() is used to sort the elements in a list, usually alphabetically
#.reverse() is used to reverse the elements in a list. Using this will not reverse in alphabetical order rather it will reverse in its original order
#.clear() is used to empty a list
#.index() is used to return the index of an element in a list
#.count() is used to count the number of instances of an element in a list because a list allows for duplicates



fruits.append("grape")
print(fruits)       #The result will be: ["apple", "orange", "banana", "coconut", "pineapple", "grape"] 

fruits.remove("coconut")
print(fruits)       #

fruits.insert(2, "carrot")
print(fruits)

fruits.insert("mango")  # This will not work because the argument is incomplete
print(fruits)

fruits.sort()
print(fruits)

fruits.reverse()
print(fruits)

fruits.clear()
print(fruits)

print(fruits.index("banana"))

print(fruits.append("coconut"))

print(fruits.count("coconut"))





#print(fruits)




















































































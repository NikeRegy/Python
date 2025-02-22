# Collection = single "variable" used to store multiple values
# List = [] ordered and changeable. Duplicates OK
# Set = {} unordered and immutable, but Add/Remove OK. NO duplicates
# Tuples = () ordered and unchangeable. Duplicates OK. FASTER


# SETS
# Sets are stored in curly brackets, they don't have an order, the order changes as many times as you run the set.
# Indexing on a set is not possible because of the unordered nature of sets.
# Even when you have a duplicate in your set, when you run the code, it won't show the duplicate value in your result
# Intersection of 2 sets can be found through the following methods:
# - using the & operator i.e intersecton = set1 & set2; print(intersection)
# - use the .intersection() function i.e set1.intersect(set2)
# - intersection_update() to modify just one of the sets i.e set1.intersection_update(set2); print(set1)


'''
.add() is used to add elements to a set 
.remove() is used to remove elements from a set
.pop() removes whatever element is first
.clear() is used to empty out a list



'''


fruits = {"apple", "orange", "mango","grape"}
'''fruits.append("pineapple")
print(fruits)'''

# print(dir(fruits))
# print(help(fruits))
# print(fruits.add("coconut"))
# print(fruits.remove("orange"))
# print(len(fruits))
# fruits.add("avocado")
# fruits.remove("orange")
# fruits.pop()
# fruits.clear()








print(fruits)



# Note: Sets are mutable except for frozen sets which cannot be edited and are mostly used as keys in dictionaries 
















































































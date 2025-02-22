# 2D stands for 2 Dimensional : Its a list that contains lists

'''fruits = ["apple", "orange", "banana", "coconut"]
vegetables = ["celery", "carrots", "potatoes"]
meat = ["chicken", "fish", "turkey"]


groceries = [fruits, vegetables, meat]'''

#print(groceries)

# Printing an element from a 2D list using indexing is quite differnt from using a 1-dimensional list. In the sense that the index references the lists inside i.e groceries[0] will give you the element of the fruits list.
# To reference a single element in a 2D list, you have to make use of 2 indices i.e to call out banana in the fruits list, you'll have something like (groceries[0][2])
#  To iterate over the elements of a 2D list, use nested loops

'''for collection in groceries:
   for food in collection:
      print(food, end=" ")
print()'''
    

# 2D Tuple is the same as a 2D ists i.e a tuple that contains tuples. Same for sets
# Note that a 2D tuple can contain both lists, tuples and sets

#EXERCISES

num_pad = ((1, 2, 3),
           (4, 5, 6),
           (7, 8, 9),
           ("*", 0, "#"))

for row in num_pad:
   for num in row:
      print(num, end=" ")


    





















































































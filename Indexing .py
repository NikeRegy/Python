# Indexing = accessing elements of a sequence using [] (indexing opeartor)
# characters can be accessed using the [START : END : STEP] metod
# indexing begins from 0 instead of 1 while negative indexing calls ebgins from -1, the last character in the variable
# you can index over a range [start:end] where 'start' represents where you want the range to begin from and 'end' is the character after where you want the range to end. (The end point is always exclusive)
# the START method is used when you want your range to begin from the first character i.e [:4]
# the END method is used when you want your range to cover anywhere in your variable but get to the end i.e [4:]
# the STEP method is used if you want to group the range in 2's or 3's etc i.e [::2] for step of 2



credit_number = "234.292.5484"

'''print(credit_number[4])
print(credit_number[-4])
print(credit_number[:5])  # START
print(credit_number[6:])   # END
print(credit_number[::4])  # STEP'''

#last_digits = credit_number[-4:]
#print(f"XXXX-XXXX-XXXX-{last_digits}")

credit_number = credit_number[::-1] # This reverses the order of the numbers 
print(credit_number)
 





































































































#name = input("Enter your full name: ")

#result = len(name)
# len returns the number of characters in a string
#print(result)

# .find will return the first occurence of any given variable
# .rfind is reverse of the normal .find so it returns the first occurence from behind
# .rfind will always return -1 if a value is not in a given variable 
# .capitalize will capitalize the first letter of a string variable
# .upper will make all letters in the variable uppercase
# .lower will make all letters in the variable lowercase
# .isdigit returns true or false if it contains digits. It was only return true if the variable only contains digits (it only works for string variables, casting the variables as a float or an int will give an error)
# .isaplha does the same as .isdigit but for alphabets
# .count counts the number of a specified character within a string
# .replace helps to replace any character with another

'''info = input("Enter your ID: ")
phone_number = input("Enter your phone number: ")
phone_number = phone_number.replace("-", " ")
 

print(phone_number)'''

# To get a comprehensive list of all the string methods, use print(help(str))
print(help(str))
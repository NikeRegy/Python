import time

# my_time = int(input("Enter the time in seconds: "))

'''for x in range (0, my_time):
    print(x)
    time.sleep(5)



print("TIME'S UP")'''





my_time = input("Enter the time in seconds: ")

for x in reversed(range (0, int(my_time))):
    seconds = x % 60
    minutes = int(x / 60) %  60
    hours = int(x / 3600)
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(0.5)

# Counting is steps can also be a way to reverse 

print("TIME'S UP")
 



























































































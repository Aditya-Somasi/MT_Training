sum = 0

while True:
    num = int(input("Enter a number (enter a negative number to stop): "))

    if num < 0:
        break  
    sum += num 

print("The sum of all positive numbers is: ", sum)

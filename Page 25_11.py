import math
num = input("Enter a number: ")
i = 1
m = 10
while int(num) > m:
    i += 1
    m *= 10
print(f"The number of digits in numeric is: {i}")

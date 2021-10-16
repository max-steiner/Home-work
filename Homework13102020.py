
'''
#Page 38 ex. 8
l = input("Enter the number of lines and number of columns separated by comma: ").split(", ")
for x in range(int(l[0])):
    print("*  " * int(l[1]))
'''

'''
#Page 35  ex. 1
n = 0
x = 0
for i in range(0, 100):
    m = int(input(f"Enter a number {i + 1}: "))
    if n <= m:
        n = m
        x += 1
    else:
        print("Data is not sorted")
        break
if x == 100:
    print("Data is sorted")
'''


'''
#Page 26 ex. 16
a = int(input("Enter a first number: "))
b = int(input("Enter a second number: "))
pr = 0
for i in range(0, a):
    pr += b
print(f"The product of two numbers is: {pr}")
'''

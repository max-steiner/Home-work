
n = int(input("Enter an integer: "))
while n > 0:
    sum = 0
    n = list(str(n))
    for i, j in enumerate(n):
        sum += int(j)
    print(f"The number you entered consists of {i + 1} digits, the sum of which is {sum}.")
    n = int(input("Enter an integer: "))

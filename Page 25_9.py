big = int(input("Enter a number № 1: "))
i = 2
while i <= 5:
    small = int(input(f"Enter a number № {i}: "))
    if big < small:
        big = small
    i += 1
print(f"The biggest number is: {big}, index: {i}")

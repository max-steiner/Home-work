#3. input a number from the user
#   check if the number has 2 digits, if so print the ahadot digit
#    you MUST use 1 if (+and)

a = float(input("Enter any number: "))
a = abs(a)
if a / 10 >= 1 and a / 10 < 10:
    print("number of units in the number: ", a % 10)
else:
    print("this is not a two-digit number")

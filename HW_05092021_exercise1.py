# 1. input a number check if it is divided by 10 without reminder
#    you need to check if it is % 5 and % 2 == 0, if so print ('can be divided by 10')

a = float(input("Enter any number "))
a = abs(a)
if a % 2 == 0 and a % 5 == 0:
    print("The number you entered is divisible by 10")
else:
   print("The number you entered isn't divisible by 10")


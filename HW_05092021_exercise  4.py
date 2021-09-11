#4. input a number from the user
#     check if the number ahadot and asarot digit are equal and they are (both) above 1
#     you MUST use 1 if (+and)

a = float(input("Enter any number: "))
# calculate the number of units:
a1 = abs(a) % 10
# calculate the number of tens:
a10 = (abs(a) // 10) % 10
if a1 == a10 and a1 == a10 > 1:
    print("The number of units and tens digit are equal and they are (both) above 1")
else:
    print("condition not met")
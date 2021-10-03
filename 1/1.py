#מחלק המשותף הגדול ביותר
#greatest common factor

#-----לפי משפט אווקלידי-------
lst = list(map(float, input("Enter two numbers separated by a space. At the end press \'Enter\': ").split()))
a1 = a = max(lst)
b1 = b = min(lst)
reminder = a % b
if reminder == 0:
    print(f"The greatest common factor (GCF) of {a1} and {b1} ------> is {b}.")
else:

    while reminder != 0:
        a = b
        b = reminder
        reminder = a % b
        if reminder == 0:
         break
    print(f"The greatest common factor (GCF) of {a1} and {b1} ------> is {b}.")

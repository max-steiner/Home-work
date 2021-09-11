#2. input a number. check if the number is 0 or 1, if so print '0 or 1'
#    otherwise check if the number is -1, if so print '-1'
#    otherwise print 'unknown number'

a = float(input("Enter any number "))
if a == 0 or a == 1:
    print("The number you entered is ", a)
else:
    if a == -1:
        print("The number you entered is ", a)
    else:
        print("Unknown number")
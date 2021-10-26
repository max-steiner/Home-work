#2. Checking the correctness of the sum of two numbers
'''
_sum = input("Enter an example of summing two numbers by pattern: a + b = c: ").strip().split()
print(f"The result you received is : {int(_sum[0]) + int(_sum[2]) == int(_sum[-1])}")
'''

# If I have a list of numbers, for example [100, 8, 7, 5, 1] and I want to go through a loop on half
#the first numbers, how do I write that?
'''
lst = list(input("Enter your list of numbers: ").split())
hAlf = round(len(lst) / 2)
for x in range(0, hAlf):
    print(lst[x])
'''


#4. Create a list of sample words: [‘coding of world’, ‘pen’, ‘python’, ‘hello' ]. Write a loop that passes
#on the list and prints each word in capital letters
'''
lst = input("Enter a list of words separated by a space: ").split()
for x in lst:
    print(x.upper())
'''

#5. Change Exercise 4. If you come across a word shorter than 4 letters, exit the loop
'''
lst = input("Enter a list of words separated by a space: ").split()
for x in lst:
    print(x.upper())
    if len(x) < 4:
        break
print("You entered a word consisting of less than 4 letters")
'''


#10 * .Challenge: Create a list of numbers. For example: [100, 8, 7, 5, 1]. Write a loop that goes over the list
#and finds the largest number (without using the max function)
'''
lst = input("Enter a list of numbers separated by a space: ").split()

def get_max_min(s):
    s1 = sorted(s)
    print(f"Maximum value in list is: {s1[-1]}.\nMinimum value in list is: {s1[0]}")


get_max_min(lst)
'''


#11.List from lists
'''
lst = [[4, 8, 200], [4, 3000, -1], [5, 87, 12]]


def get_max_min(lst):
    lst_open = [x
        for row in lst
        for x in row
               ]
    lst_open_sorted = sorted(lst_open)
    _max = lst_open_sorted[-1]
    _min = lst_open_sorted[0]
    print(f"Maximum value in list is: {_max}.\nMinimum value in list is: {_min}")


get_max_min(lst)
'''

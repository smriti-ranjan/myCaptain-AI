#Write a Python program to print all positive numbers in a range.
#Your Input and output must look something like this
"""Input: list1 = [12, -7, 5, 64, -14] Output: 12, 5, 64
Input: list2 = [12, 14, -95, 3] Output: [12, 14, 3]"""


list1 = [12, -7, 5, 64, -14]
list2 = [12, 14, -95, 3]

for i in list1:
    if i>=0:
        print(i, end = ', ')
        
print('\n')

for i in list2:
    if i>=0:
        print(i, end = ', ')

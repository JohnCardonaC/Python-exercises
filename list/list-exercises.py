
# 1. Write a Python program to sum all the items in a list.

enteros = [1, 2, 3, 4, 5, 7, 10]
sumNumbers = 0
for i in enteros:
    sumNumbers += i
print(sumNumbers)


# 2. Write a Python program to multiply all the items in a list

enterosMult = [5, 2, 5]
multNumbers = 1
for x in enterosMult:
    multNumbers *= x
print(multNumbers)


# 3. Write a Python program to get the largest number from a list.
list3 = [2, 12, 4523, 2, 1234, 1892, 9182738912]
maxNum = [0]
for i in list3:
    if (i > maxNum):
        maxNum = i
print(maxNum)


# 4. Write a Python program to get the smallest number from a list.

list4 = [12, 4523, 1234, 1892, 5, 9182738912]
minNum = list4[0]
for i in list4:
    if (i < minNum):
        minNum = i
print(minNum)


''''
5. Write a Python program to count the number of strings from a given list of strings. The string length is 2 or more and the first and last characters are the same.

Sample List : ['abc', 'xyz', 'aba', '1221']

Expected Result : 2
'''

list5 = ['abc', 'xyz', 'aba', '1221',
         "asjkl", "jkshda", "raskjr", "ee",  "eae"]
countList = 0
for x in list5:
    if ((x[0] == x[-1]) and (len(x) > 2)):
        countList += 1
print(countList)

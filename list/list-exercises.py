
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

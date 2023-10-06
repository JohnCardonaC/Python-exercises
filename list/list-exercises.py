
# 1. Write a Python program to sum all the items in a list.

from random import shuffle
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


''''
6. Write a Python program to get a list, sorted in increasing order by the last element in each tuple from a given list of non-empty tuples.

Sample List : [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]

Expected Result : [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]
'''

list6 = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
# list6 = [1, 3, 5, 75, 23]
def last(n): return n[-1]


list6.sort(key=last)
print(list6)


# 7. Write a Python program to remove duplicates from a list.
list7 = ["1", "4", "7", "4", "4", "4", "4"]
noDiplictaeList = []

for i in list7:
    if i not in noDiplictaeList:
        noDiplictaeList.append(i)
noDiplictaeList.sort()
print(noDiplictaeList)


# 8. Write a Python program to check if a list is empty or not.
list8 = []
if len(list8) == 0:
    print("La lista está vacia")
else:
    print("La lista no está vacia")

# 9. Write a Python program to clone or copy a list.
original_list9 = [10, 22, 44, 23, 4]
new_list9 = list(original_list9)


# 10. Write a Python program to find the list of words that are longer than n from a given list of words.
list10 = ["hola", "No", "yes", "Multifuncional",
          "Esfero", "Memoria", "Universidad", ]
n = 3
for i in list10:
    if len(i) > n:
        print(i)


# 11. Write a Python function that takes two lists and returns True if they have at least one common member.

list11a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list11b = [1,  102, 123, 43, 45]
comp = False

for i in list11a:
    for x in list11b:
        if i == x:
            comp = True
            break
print(comp)


# 12. Write a Python program to print a specified list after removing the 0th, 4th and 5th elements.

list12 = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
list12.pop(0)
list12.pop(3)
list12.pop(3)

print(list12)

# Se resta un valor en cada pop ya que al eliminar un elemento de la lista el len cambia


# 14. Write a Python program to print the numbers of a specified list after removing even numbers from it.

list14 = [2, 312, 1, 45, 234, 6345, 765, 7632, 13, 16]
num = [x for x in list14 if x % 2 != 0]
print(num)


# 15. Write a Python program to shuffle and print a specified list.

color = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
shuffle(color)
print(color)

# 16. Write a Python program to generate and print a list of the first and last 5 elements where the values are square numbers between 1 and 30 (both included).
list16 = []
for i in range(1, 6):
    list16.append(i**2)
for x in range(26, 31):
    list16.append(x**2)
print(list16)

""""
17. Write a Python program to check if each number is prime in a given list of numbers. Return True if all numbers are prime otherwise False.
Sample Data:
([0, 3, 4, 7, 9]) -> False
([3, 5, 7, 13]) -> True
([1, 5, 3]) -> False
"""

list17 = [3, 11, 13, 17]
primo = True
for i in list17:
    for x in range(2, i):
        if i % x == 0:
            primo = False
            break
print(primo)

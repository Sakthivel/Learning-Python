# *** Lists ***
#  A list is created by placing all the items (elements) inside a square bracket [ ]
#  onPacking available in list

# myList = ['sakthi', 'vel', 'blr', 'salem', 'london']
# print(myList) output:- ['sakthi', 'vel', 'blr', 'salem', 'london']

# print(myList[:])  output:- ['sakthi', 'vel', 'blr', 'salem', 'london']

# print(myList[1]) output:- vel

# print(myList[1:])  output:- ['vel', 'blr', 'salem', 'london']

# print(myList[2:4])  output:- ['blr', 'salem']

# print(myList[:3])  output:- ['sakthi', 'vel', 'blr']

# [] it wont change the original list/string and returns new list/string

# *** 2D lists ***

# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]

# print(matrix[0][1]) output: 2
# matrix[0][1] = 20
# print(matrix[0][1]) output: 20

# *** list loop ***
# for row in matrix:
#     for item in row:
#         print(item)

# numbers = [5, 1, 3, 7, 4, 5]

# numbers.append(20)

# numbers.insert(0, 10)

# numbers.remove(5)

# print(numbers) output:- [10, 1, 3, 7, 4, 20]

# numbers.clear()
# print(numbers) output:- []

# numbers.pop();  // remove last element in the list
# print(numbers);  input:- [5, 1, 3, 7]

# print(numbers.index(5))  output:- 0  return the element index here

# print(50 in numbers) output:- false this is the way to check the element is there in the list

# print(numbers.count(5)) output:- 2 return how many `5` occured in the list

# numbers.sort()
# print(numbers) to sort/ ascending order the list use sort() method

# numbers.reverse()  to reverse the list use reverse()
# print(numbers);

# numbers2 = numbers.copy() # copy() used for duplicate the list and it wont talk each other. The both list will work independently
# numbers2.append(8)
# print(numbers2)
# print(numbers)

# Exercise remove duplicate items in the list
# uniques = []
# for number in numbers:
#     if number not in uniques:
#         uniques.append(number)
# print(uniques) output:- [5, 1, 3, 7, 4]
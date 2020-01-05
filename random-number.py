# *** Generating Random Values ***

# Python 3 module index ref:- https://docs.python.org/3/py-modindex.html

# import random

# for i in range(3):
#     print(random.random())  // output:- 0.6678902345
#     print(random.randint(10, 20)) // output:- random number between 10 to 20

# members = ['Sakthi', 'Vel', 'Kumar', 'Kanthan', 'Mailan']
# leader = random.choice(members)   // it will pick name from the list by random
# print(leader)

# execise:- Roll a dice, get random two values like (3, 1). We have to create a class and we have to use tuples also.

# import random
#
#
# class Dice:
#     def roll(self):
#         first = random.randint(1, 6)
#         second = random.randint(1, 6)
#         return first, second
#
#
# dice = Dice()
# output = dice.roll()
# print(output)  // Output:- (random number, random number) like (6, 1)
#  *** Constructors   ***

#  def __init__(self) is the constructor method in Python. It will execute when create an object/instance.
#  constructor method  `self` parameter hold the object ref. so it mismatch if we have more objects

#  example
# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def move(self):
#         print('move')
#
#     def draw(self):
#         print('draw')
#
#
# point1 = Point(10, 20)
# print(point1.x)  // output:- 10

# Exercise
# class Person:
#     def __init__(self, name):
#         self.name = name
#
#     def talk(self):
#         print(f'Hi, I am {self.name}!')
#
#
#
# person = Person('Sakthi')
# person.talk()  // output:- Hi, I am Sakthi!
# person1 = Person('Vel')
# person1.talk()   // output:- Hi, I am Vel!
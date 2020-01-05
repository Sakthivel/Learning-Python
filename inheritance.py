#  *** Inheritance   ***
#  Inheritence is a concept in Object oriented programming. Basically child class try to call/use parent class's methods
#  Python inheritence syntax: pass Parent ClassName into Child Class parentheses ex. class Dog(Mammal):
#  pass means class is not having etc method apart from Parent Class we are using else not required.
#  Python throw warning child class name not having extra methods apart from Parent Class methods
#
# class Mammal:
#     def walk(self):
#         print('walk')
#
#
# class Dog(Mammal):
#     def bark(self):
#         print('bark!')
#
#
# class Cat(Mammal):
#     pass
#
#
# dog = Dog()
# cat = Cat()
# dog.bark() // output:- bark
# cat.walk() // output:- walk
# dog.walk() // output:- walk
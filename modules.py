#  *** Modules   ***

# The same kind of functionality club into a single file and import the file wherever we want it
# There are two way of import like all methods and method which we want it

# option:- 1
# import converters
# print(converters.kg_to_lbs(72))   // output:- 160.0
# print(converters.lbs_to_kg(180))  // output:- 81.0

# option:- 2
# from converters import lbs_to_kg
# print(lbs_to_kg(180))  // output:- 81.0

# Exercise
# import utils
# number_list = [1, 3, 5, 2, 90, 76, 45, 55]
# print(utils.find_max(number_list))  // output:- 90
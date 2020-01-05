
#  *** Functions  ***
# Function is some block code which will execute when we call the method. def is a keyword to define a function in Python
# eg:-
# def greet_user():
#     print('Hello')
#
#
# greet_user()
# And we need to give two new line break to close/complete the function statement. Calling function will like this -> greet_user() but
# we can't call the method before define the method

# def greet_user():
#     print("Hello!")
#     print("How are you doing?")
#
#
# print("Start Function")
# greet_user()
# print("End Function")

#  *** Parameters  ***
#   Parameters are which is receive information in the function
#   Arguments are which is passing information to the function
# def greet_user(name):
#     print(f"Hello {name}!")
#     print("How are you doing?")
#
#
# print("Start Function")
# greet_user("Sakthi")
# print("End Function")

#  *** Keyword Arguments  ***
#   Arguments are which is passing information to the function
#   Parameters are which is receive information in the function

# the blow example for `positional argument`
# def greet_user(first_name, last_name):
#     print(f"Hello {first_name} {last_name}!")
#     print("How are you doing?")
#
#
# print("Start Function")
# greet_user("Sakthi", "vel")  //positional argument; mostly/ often we will use this
# print("End Function")

# the blow example for `keyword argument`
# def greet_user(first_name, last_name):
#     print(f"Hello {first_name} {last_name}!")
#     print("How are you doing?")
#
#
# print("Start Function")
# greet_user(first_name="Sakthi", last_name="vel") // keyword argument; rarely/not often we use this
# print("End Function")

# The Python will accept mix of both arguments but keyword argument must be followed by positional arguments
# example:-
# greet_user(first_name="Sakthi", "vel") // it is not correct
# greet_user("Sakthi", last_name="vel") // it is correct

#  *** Return Statment  ***
#  Wee have to use `return` keyword to return values to caller
#  By default function/method return None

# def square(number):
#     return number * number
#
#
# print(square(3))

#  *** Creating a reuseable function  ***

# def emojis_converter(message):
#     words = message.split(' ')
#     emojis = {
#         ":)": "😀",
#         ":(": "☹️",
#         ":p": "😛"
#     }
#     output_string = ''
#     for word in words:
#         output_string += emojis.get(word, word) + " "
#     return output_string
#
#
# message = input("Enter your message > ")
# output = emojis_converter(message)
# print(output)
#  *** Dictionaries  ***

# it looks like object. Key value pair and duplicate keys are not allowed. Key is unique
# eg. customer = {
#     "name": "Sakthi",
#     "age": 30,
#     "place": "London"
# }

# customer = {
#     "name": "Sakthi",
#     "age": 30,
#     "place": "London"
# }
# print(customer['name'])  output:- Sakthi
# print(customer.get('name'))  output:- Sakthi
# print(customer['Name'])  output:- KeyError because key is unique
# print(customer.get('Name'))  output:- None. The None is an object, it means nothing to show.
# How to set default values if key is not there:
#     print(customer.get('Name', 'Vel'))  output:- Vel

# How to update the value to the key:
# customer['name'] = "Mosh"
# print(customer.get('name')) output:- Mosh

# customer['dob'] = 'Jan 20, 2009'  adding new pair into dictionaries
# print(customer.get('dob'))

#  Exercise:- enter number and show it in string ***
# number_dictionaries = {
#     "1": "one",
#     "2": "two",
#     "3": "three",
#     "4": "four",
#     "5": "five"
# }
# output_string = ''
# phone = input('Please enter the numbers within 5? ')
#
# for number in phone:
#     output_string += number_dictionaries.get(number, '!') + " "
# print(output_string)

#  *** Emoji Converter ***
# message = input(">")
# words = message.split(' ')
# emojis = {
#     ":)": "😀",
#     ":(": "☹️",
#     ":p": "😛"
# }
# output_string = ''
# for word in words:
#     output_string += emojis.get(word, word) + " "
# print(output_string)
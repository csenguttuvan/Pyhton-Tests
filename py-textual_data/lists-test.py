import re
"""value = input('Enter your favorite colour: ')"""


value = input('Enter your favorite colour: ')
value_2 = input('Enter your favorite fruit ')
value_3 = input('Enter your favorite adjective: ')
if not re.match("[a-z]", value):
    print('Error, please enter a string')
else:
    print('{} {} are {}'.format(value, value_2, value_3).capitalize())


















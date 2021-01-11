import re


value = str(input('Enter your favorite colour: '))
if not re.match('[a-z]', value):
        print('Letter only')
elif len(value) > 15:
    print('Error!, 15 Characters only')



#while True:
    #try:
        # Note: Python 2.x users should use raw_input, the equivalent of 3.x's input
        #age = int(input("Please enter your age: "))
    #except ValueError:
        #print("Sorry, I didn't understand that.")
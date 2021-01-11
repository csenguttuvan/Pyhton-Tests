name = input("Enter your name: ")
length = (len(name))
greeting = "Hello"
if name =="chris":
    print("{} {}, I've been expecting you".format(greeting, name.capitalize()))

else:
    text = "{}, {}, Welcome!".format(greeting, name.capitalize())
    text2 = "The length of your name is: {}".format(length)
   
      
    print(text)
    print(text2)

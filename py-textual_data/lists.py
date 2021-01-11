courses = ['science', 'maths', 'PE', 'biology']
courses.append('art') #adds to the list
courses.insert(5, 'music') #adds list with position and vlaue as the argument
courses2 = ['RE', 'English']
courses.extend(courses2) #add more that 2 values to the list
courses.reverse() #prints the list in reverse
nums = [1,3,6,7,8,9]
#print(courses[0:3]) #print all the values from 0-3 but not including 3
print(sum(nums)) #prints the value of nums variable
course_str = ', '.join(courses) #convert a list into a string value
print(course_str)
print(courses.index('maths')) #check index number of value in the list

for values in courses:
    print(values)
    
print('maths' in courses) #checks whether the value maths is in the list.
print(courses)

cs_courses = {'History', 'Math', 'Physics', 'CompSci'}
other_courses = {'History', 'science', 'Physics', 'geology'}

print(cs_courses.intersection(other_courses)) #check what values are in both sets and prints them

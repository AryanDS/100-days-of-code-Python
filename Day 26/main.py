"""
List comprehension
new_list=[new_item for item in list]
"""

#new_list=[new_item for item in list]
numbers=[1,2,3,4]

new_list=[i+2 for i in numbers]

print(new_list)

letters= "Aryan"

new_list_letter =[let for let in letters]
print(new_list_letter)

"""
Python Sequence are LIST, TUPLES, RANGE, STRING
"""

range_list =[i*2 for i in range(1,5)]
print(range_list)


"""
Conditional list comprehension

new_list=[new_item for item in list if test]
add items to the new list only when the 'if test' condition is TRUE
"""

names =["Aryan","Anushka","Ishant","Pranav"]

names_list=[i for i in names if len(i)>5]
print(names_list)

upper_names_list = [i.upper() for i in names if len(i)<6]
print(upper_names_list) 


"""
Dictionary Comprehension
Creating a new dictionary by using items in the list.
new_dict={new_key:new_value for item in list}

Creating a new dictionary by using items in another dictionary
new_dict={new_key:new_value for (key, value) in dict.items()}

With condition
new_dict={new_key:new_value for (key, value) in dict.items() if test}

"""

import random

new_dict ={name:random.randint(0,100) for name in names}
print(new_dict)

passed_students={key:value for (key,value) in new_dict.items() if value>60}

print(passed_students)



"""
Iterating over a Pandas data frame

"""

student_dict={
    "Student":["Aryan","Anushka","Aarya"],
    "Marks":[99,99,99]
}

import pandas as pd

student_df = pd.DataFrame(student_dict)
print(student_df)

#Iterating through a pandas dataframe 
for key,value in student_df.items():
    print(key)
    print(value)

#Not particularly useful
# Using Iterrows!

for index, row in student_df.iterrows():
    # print(index)
    # print(row) 

    print(row.Student) 
    print(row.Marks)  
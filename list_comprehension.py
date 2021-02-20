
# List Comprehension - Exclusive to Python

# Create a new list from a previous list without list comprehension:

# numbers = [1,2,3]
# new_list = []
# for n in numbers:
#     add_1 = n + 1
#     new_list.append(add_1)
# print(new_list)

# # List comprehension looks like this 

# # new_list = [new_list for item in list] <-- keyword example

# # replace 'list' keyword with actual list
# # new_list = [new_list for item in numbers]

# # each item in the list (can be called anything, in this example it is called n)
# # new_list = [new_list for n in numbers]

# # Final keyword to replace is 'new_item' - its whatever you want the new item to be in your list.
# # In this example it is n + 1
# new_list = [n + 1 for n in numbers]

# # List comprehension working with strings
# name = "Angela"
# letters_list = [letter for letter in name]
# print(letters_list) # ['A', 'n', 'g', 'e' 'l', 'a']


# List comprehension working with range
# new_range = [num * 2 for num in range(1, 5)]
# print(new_range) # [2, 4, 6, 8]

# Conditionals "If/Else" List Comprehension

# new_list = [new_item for item in list if test] <-- keyword example

# names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]

# # Get names with 4 letters or less

# # short_names = [name for name in names if len(name) < 5]
# # print(short_names)

# big_names = [name.upper() for name in names if len(name) > 5]

# print(big_names)

# Dictionary Comprehension

# new_dict = {new_key:new_value for item in list} <-- syntax keyword example

# Dictionary comprehension is just a way of creating a dictionary using this shortened syntax

# Could take it one step further like this:
# By creating a new Dictionary based on the values in an existing dictionary
# new_dict = {new_key:new_value for (key, value) in dict.items()}

# Another step further would be to include a coniditon at the end of our syntax keywords like below:
# new_dict = {new_key:new_value for (key, value) in dict.items() if condition}

# import random
# names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]

# students_scores = {student:random.randint(1,100) for student in names}
# # student_scores = {'Alex': 19, 'Beth': 42, 'Caroline': 100, 'Dave': 96, 'Eleanor': 80, 'Freddie': 57}
# print(students_scores)

# passed_students = {student:score for (student, score) in students_scores.items() if score > 60}
# print(passed_students)

student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}
# Looping through dictionaries:
# for (key, value) in student_dict.items():
#     print(key)

# Looping through DataFrame:
import pandas
student_data_frame = pandas.DataFrame(student_dict)

for (key, value) in student_data_frame.items():
    print(value)
# This isnt particularly useful 
# But pandas has an in-built loop that will Loop through ROWS
for (index, row) in student_data_frame.iterrows():
    print(row)

for (index, row) in student_data_frame.iterrows():
    if row.student == "Angela":
        print(row.score)










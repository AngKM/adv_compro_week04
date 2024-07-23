# #Ex1
# # 1.    Define an integer variable named age and set it to 25.
# # 2.    Define a float variable named height and set it to 5.9.
# # 3.    Define a string variable named name and set it to your name.
# # 4.    Define a boolean variable named is_student and set it to True.
# # 5.    Print all the variables.

# age = 25
# height = 5.9
# name = "Ang"
# is_student = True
# print(name,age,height,is_student)



# #Ex2
# sentence = "Python programming is fun"
# print(sentence.upper())
# new_sentence = sentence.replace("fun", "awesome")
# print(new_sentence)
# print(sentence.split())



# Assignment 3: List append() Method
# Objective: Understand how to add elements to a list using append().

#     1.    Create an empty list named colors.
#     2.    Use the append() method to add “red”, “green”, and “blue” to the list.
#     3.    Print the list.
#     4.    Append “yellow” and “purple” to the list.
#     5.    Print the length of the list.

# colors = []
# colors.append("red")
# colors.append("green")
# colors.append("blue")
# print(colors)
# colors.append("yellow")
# colors.append("purple")
# lengths = len(colors)
# print(lengths)



# Assignment 4: List remove() Method
# Objective: Learn how to remove specific elements from a list using remove().

#     1.    Create a list named animals containing “cat”, “dog”, “rabbit”, “bird”, “fish”.
#     2.    Use the remove() method to remove “rabbit” from the list.
#     3.    Print the list.

# animals =  ["cat", "dog", "rabbit", "bird", "fish"]
# animals.remove("rabbit")
# print(animals)



# Assignment 5: List insert() Method
# Objective: Learn how to insert elements at specific positions in a list using insert().

#     1.    Create a list named numbers containing the integers 1, 2, 4, 5, 6.
#     2.    Use the insert() method to add the number 3 between 2 and 4.
#     3.    Print the list.
#     4.    Insert the number 0 at the beginning of the list.
#     5.    Print the final list of numbers.
# numbers = [1,2,4,5,6]
# numbers.insert(2, 3)
# print(numbers)
# numbers.insert(0, 0)
# print(numbers)


# Assignment 6: List pop() Method
# Objective: Understand how to remove elements from a list using pop() and how to use the removed elements.
#     1.    Create a list named cities containing “New York”, “Los Angeles”, “Chicago”, “Houston”, “Phoenix”.
#     2.    Use the pop() method to remove the last element from the list and store it in a variable.
#     3.    Print the variable holding the removed element.
#     4.    Use pop() to remove the first element from the list.
#     5.    Print the final list of cities.

# cities = ["New york", "Los Angeles", "Chicago", "Houston", "Phoenix"]
# last_city = cities.pop()
# print(last_city)
# first_fruit = cities.pop(0)
# print(cities)



# Assignment 7: List sort() Method
# Objective: Learn how to sort elements in a list using sort().

#     1.    Create a list named scores containing the following numbers: 88, 92, 75, 89, 78.
#     2.    Use the sort() method to sort the list in ascending order.
#     3.    Print the sorted list.
#     4.    Sort the list in descending order and print it.
#     5.    Create a list of strings named names containing “Alice”, “Bob”, “Charlie”, “David”, “Eve” and sort it in alphabetical order.

# scores = [88, 92, 75, 89, 78]
# scores.sort()
# print(scores)
# scores.sort(reverse=True)
# print(scores)
# names = ["Alice", "Bob", "Charlie", "David", "Eve"]
# names.sort()
# print(names)



# Assignment 8: Lists
# Objective: Understand how to create and manipulate lists in Python.

#     1.    Create a list named fruits containing “apple”, “banana”, “cherry”.
#     2.    Add “orange” to the list.
#     3.    Remove “banana” from the list.
#     4.    Sort the list in alphabetical order.
#     5.    Print the length of the list.

# fruits = ["apple", "banana", "cherry"]
# fruits.append("orange")
# fruits.remove("banana")
# fruits.sort()
# str_length = len(fruits)
# print(str_length)



# Assignment 9: List Slicing
# Objective: Learn how to slice lists to access sublists.

#     1.    Create a list named letters containing the first 10 letters of the alphabet. Ex. [A, B, C, D, ... ]

#     2.    Slice the list to get the first 5 letters and print the result.
#     3.    Slice the list to get the last 5 letters and print the result.
#    4.    Reverse the list and print the result.
# letters = ["A","B","C","D","E","F","G","H","I","J"]
# first_five = letters[0:5]
# last_five = letters[5:]
# first_five.reverse()OP
# last_five.reverse()
# print(first_five)
# print(last_five)
# print(letters[::-1])



# Assignment 10: Dictionary Basics
# Objective: Learn how to create and use dictionaries in Python.

#     1.    Create a dictionary named student with keys: “name”, “age”, “grade”.
#     2.    Set the values of the dictionary to your name, age, and a grade of your choice.
#     3.    Print the dictionary.
#     4.    Add a new key-value pair: “school” with the value of your school name.
#     5.    Remove the key “grade” from the dictionary and print the updated dictionary.

# student ={
#     "name":"Ang",
#     "age":19,
#     "grade":6.9
# }
# print(student)
# student["school"] = "SIIE"
# del student["grade"]
# print(student)

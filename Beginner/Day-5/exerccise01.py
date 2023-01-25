'''
Instructions
You are going to write a program that calculates the average student height from a List of heights.
The average height can be calculated by adding all the heights together and dividing by the total number of heights.
'''
# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])

total_heights = 0
for height in student_heights:
    total_heights += height
print(total_heights)

number_of_students = 0

for student in student_heights:
    number_of_students += 1
average_heights = round(total_heights / number_of_students)

# average_heights = round(total_heights / len(student_heights))
print(average_heights)
'''
# Get inputs as Strings
input_string = input('Enter elements of a list separated by space ')
print("\n")
# create a list and split the strings as a data
user_list = input_string.split()
# print list
print('list: ', user_list)

# convert each item to int type
for i in range(len(user_list)):
    # convert each item to int type
    user_list[i] = int(user_list[i])

# Calculating the sum of list elements
print("Sum = ", sum(user_list))
'''

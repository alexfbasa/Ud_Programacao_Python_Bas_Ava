'''
You are going to write a program that calculates the average student height from a List of heights.
e.g. student_heights = [180, 124, 165, 173, 189, 169, 146]
The average height can be calculated by adding all the heights together and dividing by the total number of heights.
e.g.
180 + 124 + 165 + 173 + 189 + 169 + 146 = 1146
There are a total of 7 heights in student_heights
1146 ÷ 7 = 163.71428571428572
Average height rounded to the nearest whole number = 164
Important You should not use the sum() or len() functions in your answer. You should try to replicate their functionality using what you have learnt about for loops.
'''

student_heights = []
# Next line will produce a SINGLE  string with all the heights
get_student_heights = input("Input a list of student heights. ").split()
print(get_student_heights)

total_heights = 0
for h in get_student_heights:
    total_heights += 1
print(total_heights)
for student in get_student_heights:
    student_x = float(student)
    student_heights.append(student_x)

total = 0
for height in student_heights:
    total += height

get_student_heights_media = round(total / total_heights)
print(get_student_heights_media)

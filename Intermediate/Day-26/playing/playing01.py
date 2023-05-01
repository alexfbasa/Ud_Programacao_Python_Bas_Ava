number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
new_list = [n * 1 for n in number_list]
print(new_list)

range_list = [n * 2 for n in range(1, 20) if n % 2 == 0]
print(range_list)

names_list = ['alex', 'beth', 'eleanor', 'robert']

names_list_upper = [name.upper() for name in names_list]
print(names_list_upper)

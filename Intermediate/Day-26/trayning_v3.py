with open('file01.txt') as file01:
    data_file01 = file01.readlines()


with open('file02.txt') as file02:
    data_file02 = file02.readlines()

result = [int(n) for n in data_file01 if n in data_file02]
# Write your code above 👆

print(result)

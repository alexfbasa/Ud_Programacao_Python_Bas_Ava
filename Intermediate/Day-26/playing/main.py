with open("file01.txt") as file01:
    file01_content = file01.read().split()
    number_file01 = [int(number) for number in file01_content]
    print(number_file01)

with open("file02.txt") as file02:
    file02_content = file02.read().split()
    number_file02 = [int(number) for number in file02_content]
    print(number_file02)

new_list = [number for number in number_file01 if number in number_file02]
print(new_list)

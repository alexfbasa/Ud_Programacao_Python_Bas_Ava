# Data Types
# String
print("Hello"[0])
print("Hello"[4])
print("123" + "234")

# Integer
print(123 + 234)
giant = 123_456_789
print(giant)

# Float
float01 = 3141.59
print(float01)
print(type(float01))

# Boolean
is_in_estonia = True
is_married = False
if is_in_estonia:
    print('Yes')
if not is_married:
    print('Noooo')

# Type Error
num_char = len(input("What is your name? "))
# print('Your name has ' + num_char + 'characters') - Str com Int
size_name = str(num_char)
print('Your name has ' + size_name + ' characters')
a = str(123)
print(type(a))

print(70 + float("100.5"))
print(str(70) + str(100))

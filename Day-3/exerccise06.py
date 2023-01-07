# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ").lower()
add_pepperoni = input("Do you want pepperoni? Y or N ").lower()
extra_cheese = input("Do you want extra cheese? Y or N ").lower()
# 🚨 Don't change the code above 👆

# Write your code below this line 👇

bill = 0

if size == "s":
    bill += 15
elif size == "m":
    bill += 20
else:
    bill += 25

# if add_pepperoni == "Y":
#     if size == "S":
#         bill += 2
#     else:
#         bill += 3

if add_pepperoni == 'y' and size == 's':
    bill += 2
else:
    bill += 3

if extra_cheese == "y":
    bill += 1

print(f"Your final bill is: ${bill}.")

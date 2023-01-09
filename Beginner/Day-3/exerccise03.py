# TODO 01 = Write a program that works out whether if a given number is an odd or even number
"""
Even numbers can be divided by 2 with no remainder.
e.g. 86 is even because 86 ÷ 2 = 43
43 does not have any decimal places. Therefore the division is clean.
e.g. 59 is odd because 59 ÷ 2 = 29.5
29.5 is not a whole number, it has decimal places. Therefore there is a remainder of 0.5, so the division is not clean.
The modulo is written as a percentage sign (%) in Python. It gives you the remainder after a division.
"""
# TODO 02 = {Example Input 1 = 43}  {Example Output 1 -- This is an odd number.}
get_number = int(input(f"Which number do you want to check? "))
if get_number % 2 == 0:
    print('This is an even number.')
else:
    print('This is an odd number.')

from art import LOGO
print(f'Welcome to the {LOGO}')
get_bill = float(input('What was the total bill? $'))
get_tip_value = int(input('How much tip would you like to give? 10, 12, or 15? '))
get_tip_split = int(input('How many people to split the bill? '))
tip_as_percent = get_tip_value / 100
total_tip_amount = get_bill * tip_as_percent

result = get_bill + total_tip_amount
bill_per_person = result / get_tip_split
final_amount = round(bill_per_person, 2)
print(f'Each person should pay: ${final_amount}')

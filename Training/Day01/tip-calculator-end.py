def get_tip_calculator():
    message = "Welcome to the tip calculator"
    print(message)
    total_bill = int(input("What was the total bill? "))
    get_tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
    get_people = int(input("How many people to split the bill?"))
    calc_bill_tip = total_bill * (get_tip / 100)
    total_amount = total_bill + calc_bill_tip
    amount_per_person = total_amount / get_people
    print(f"Total bill: R$ {total_bill:.2f}")
    print(f"Tip amount: R$ {calc_bill_tip:.2f}")
    print(f"Total amount (including tip): R$ {total_amount:.2f}")
    print(f"Each person should pay: R$ {amount_per_person:.2f}")


get_tip_calculator()

height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")

bmi_calc = float(weight) / (float(height) ** 2)
print(f"You bmi is : {bmi_calc:.0f}")

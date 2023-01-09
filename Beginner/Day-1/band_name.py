from art import LOGO
# TODO #1. Create a greeting for your program.
print(LOGO)
print('Welcome to the band name generator')
# TODO #2. Ask the user for the city that they grew up in.
get_city_name = input('Which city did you grow up int? \n')
# TODO #3. Ask the user for the name of a pet.
get_pet_name = input('What is the name of a pet? \n')
# TODO #4. Combine the name of their city and pet and show them their band name.
print(f"Your band name could be = {get_city_name} {get_pet_name} \nor")
print(f"Your band name could be = {get_pet_name} {get_city_name}")
# TODO #5. Make sure the input cursor shows on a new line:
# TODO # Solution: https://replit.com/@appbrewery/band-name-generator-end
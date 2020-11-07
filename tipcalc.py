print("Welcome to the tip calculator.")
bill_amount = input("What was the total bill? ")
tip_percentage = input("What percentage tip would you like to give? 10, 12, or 15? ")

bill_float = float(bill_amount)
tip_int = int(tip_percentage)

tip_decimal = tip_int / 100
tip_total = bill_float * tip_decimal
bill_plus_tip = bill_float + tip_total

total = input(f"The total cost of the bill plus tip is {round(bill_plus_tip, 2)}. How many people are you going to split this bill with? ")

split = bill_plus_tip / int(total)
split_float = split

print(f"You should all pay {round(split_float, 2)} each.")


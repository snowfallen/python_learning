print("Welcome to the tip calculator")
bill = int(input("What was the total bill?  "))
percentage = int(input("What percentage tip would you like to give ? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))

result_percentage = percentage / 100 * bill
final_bill = bill + result_percentage
split_bill = final_bill / people
final_amount = split_bill
final_amount = round(split_bill,2)
final_amount = "{:.2f}".format(split_bill)


print(f"Each person should pay: ${final_amount}")
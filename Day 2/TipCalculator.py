print("Welcome to the tip calculator")
bill = input("What was the total bill?  ")
percentage = input("What percentage tip would you like to give ? 10, 12, or 15? ")
people = input("How many people to split the bill? ")

result_percentage = int(percentage)/100*int(bill)
final_bill = int(bill)+int(result_percentage)
split_bill = int(final_bill)/int(people)
final_amount = split_bill
final_amount = round(split_bill, 2)
final_amount = "{:.2f}".format(split_bill)


print(f"Each person should pay: ${final_amount} ")
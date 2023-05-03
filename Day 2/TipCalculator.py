print (round(33.6, 1))

print("Welcome to the tip calculator")
bill = input("What was the total bill?  ")
percentage = input("What percentage tip would you like to give ? 10, 12, or 15? ")
people = input("How many people to split the bill? ")

result_percentage = int(percentage)/100*int(bill)
final_bill = int(bill)+int(result_percentage)
split_bill = int(final_bill)/int(people)



print(split_bill)
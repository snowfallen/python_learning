age = input ("What is your current age ?  ")

result_days = (365 * 90) - (365 * int(age))
result_weeks = (52 * 90) - (52 * int(age))
result_months = (12 * 90) - (12 * int(age))

print(f"You have {result_days} days, {result_weeks} weeks, and {result_months} until 90 years.")
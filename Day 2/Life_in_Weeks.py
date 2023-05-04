age = int(input("What is your current age ?  "))

result_days = (365 * 90) - (365 * age)
result_weeks = (52 * 90) - (52 * age)
result_months = (12 * 90) - (12 * age)

print(f"You have {result_days} days, {result_weeks} weeks, and {result_months} until 90 years.")
def is_leap(year):
    if year % 4 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 400 == 0:
        return True
    else:
        return False

def days_in_month(input_year: int, input_month: int):
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_leap(input_year) and input_month == 2:
        return 29
    return month_days[input_month - 1]
    # for index in range (0, len(month_days)):
    #     if input_month == index:
    #         input_month = month_days[index - 1]
        
    # return f"{input_month}"
    
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(input_year=year, input_month=month)
print(days)
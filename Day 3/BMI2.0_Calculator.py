height: float = float(input("enter your height in m: "))
weight: int = int(input("enter your weight in kg: "))
result = int(weight / (height **2))

print(round(result, 2))

if result < 18.5:
    print(f"Your BMI is {result}, you are underweight.")
elif result < 25:
    print(f"Your BMI is {result}, you have a normal weight.")
elif  result < 30:
    print(f"Your BMI is {result}, you are slightly overweight.")
elif result < 35:
    print(f"Your BMI is {result},you are obese.")
else:
    print(f"Your BMI is {result},you are clinically obese.")  




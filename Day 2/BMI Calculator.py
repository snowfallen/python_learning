height: float = float(input("enter your height in m: "))
weight: int = int(input("enter your weight in kg: "))
result: float = weight / (height * height)
print(round(result, 2))
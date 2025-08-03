print("Welcome to BMI calculator by Taher")
weight=float(input("Enter Weight in kg"))
height=float(input("Enter Height in Mtr"))
BMI=(weight)/(height)**2
print(BMI)
if BMI>28:
    print("Obese")
elif BMI>25:
    print("Over Weight")
elif BMI>18:
    print("Normal BMI")
else:
    print("UnderWeight")

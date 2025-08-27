# 🚨 Do not modify the values above
# Write your code below 👇

weight = float(input("Enter your weight: "))
height = float(input("Enter your hieght: "))
bmi = weight / (height ** 2)

if bmi < 18.5:
    print("You are under weight")
elif bmi >= 18.5:
    print("You are normal weight")
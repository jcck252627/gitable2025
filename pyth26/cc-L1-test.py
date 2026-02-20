i=0
while (i <= 10):
   print("Hello ", i)
   i += 1

s = ''
while s.lower() != "start":
 s = input("Please enter the word 'start': ")


print(5*"\nHello")



name=input("Enter you name:  ")
print("Welcome " +name +"!!")

age = input("Enter your age:  ")
if int(age) == 50:
 print("You exactly half a century or older!")
elif int(age) > 50:
 print("You are half a century or older!")
elif 20 <= int(age) <= 29:
 print("You are in your twenties")
else:
 print("your age is ", age)


num1=input("Enter your 1st number :  ")
if num1.isdigit():
    print("First Number entered is: ", num1)
else:
    print("Please input a valid interger !!")    
num2=input("Enter your 2nd number :  ")
if num2.isdigit():
    print("First Number entered is: ", num2)
else:
    print("Please input a valid interger !!")  

print ("The addition of the two numbers : ", int(num1)+int(num2))
print ("The multiple of the two numbers: ", int(num1)*int(num2))




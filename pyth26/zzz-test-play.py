import os
import sys
import datetime
import random

def get_current_date():
 cur_date = datetime.datetime.now()
 print(f"Today's date is {cur_date.month}/{cur_date.day}/{cur_date.year}")

def get_current_date2():
 cur_date = datetime.datetime.now()
 y = cur_date.year
 m = cur_date.month
 d = cur_date.day
 s = "Today's date is " + str(m) + "/" + str(d) + "/" + str(y)
 print(s)

def cube(x):
    t=print(x ** 3)
    return x ** 3

def cube2(x):
 print(x ** 4)
 return x ** 4

def total_cost(items_purchased, price_per_item):
 subtotal = items_purchased * price_per_item
 total = subtotal + subtotal * 0.05
 print(f'Your total is ${total:,.2f}')

def return_five():
    return 5

print(sys.version)
print(os.name)
print(datetime.datetime.now())
cur_date = datetime.datetime.now()

print(cur_date.year) # Prints current year
print(cur_date.month) # this month
print(cur_date.day) # today's date


print(cur_date.weekday())
day = ""
if cur_date.weekday() == 0:
 day = "Monday"
elif cur_date.weekday() == 1:
 day = "Tuesday"
elif cur_date.weekday() == 2:
 day = "Wednesday"
elif cur_date.weekday() == 3:
 day = "Thursday"
elif cur_date.weekday() == 4:
 day = "Friday"
elif cur_date.weekday() == 5:
 day = "Saturday"
else:
 day = "Sunday"
print("Today is", day)


get_current_date()
get_current_date2()

 
t=  cube(3)
print(t)
x1=  cube(3) # prints 27
x2=  cube(4) # prints 64
x3=  cube(5) # prints 125
print(x1)
print(x2)
print(x3)

for i in range(2, 6):
 cube2(i)

total_cost(10, 3)

print(return_five())

for i in range(10):
    num_asterisks = random.randint(1, 10)
    print("*" * num_asterisks)

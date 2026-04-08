
nums = []
for i in range(5):
    num = input(f'Enter number {i + 1}: ')
    while not num.isdigit():
        print("That is not a number!")
        num = input(f'Enter number {i + 1}: ')
    nums.append(num)
for i in nums:
    print(i, end=" ")




x = 0
while x < 10:
 print(x , end = ' ')
 x += 1

for i in [0, 1, 2, 3, 4, 56, 78]:
 print(i)

x = [1, 2, 3, 4]
for i in x:
 print("-------\n")
 print(i)

for i in "CIS247":
 print(i)

for aa in range (1, 100):
 print(aa)


x = []
for i in range(1, 9, 2):
 x.append(i)
print(x)

f = 1
for i in range(2, 8):
 f = f * i
print("7!=3333333333 =", f)



for i in range(1555, -1):
    print (i, end = ' ')

for i in range(15, -1, -3):
 print(i, end=' ')

for i in range(5):
 for j in range(5):
    print(j, end='')
 print()





print ("\n\n\n--------------------\n")

for i in range(5, -100, -1):
 print(i, end=' ')

a = [1, 2, 'hello', 4]
for item in a:
 print(f"Item #{item} is ", item)



print ("\n\n\n--------------------\n")
state = "California"
print(state.find("for")) 
print(state.find("a")) # Returns 1
print (state.find("xyzC")) # Returns -1
ss= state.replace("al", "b")
print(ss)



myList = [123, 3333, 1.23]
myList.append ("Hello")
print(myList)
myList.append ("Hello-remove-me")
print(myList)
myList.pop(4)
myList.pop(3)
myList.sort()
print(myList)




total_cost = 5000
monthly_payment = total_cost / 12
print(f'Your bi-monthly payment is ${monthly_payment*121 /2: ,.2f}')

age = 50
print(type(age))

print("------------------------------------------------------------\n")
print("--------------LIST COMPREHENSION----------------------------\n")      


a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
words = ["alpha", "beta", "GAMMA", "delta", "OMEGA"]
wordss = ["api", "automation", "devops", "cloud", "py"]


resa = [n for n in a if n % 2 == 0]  # print even
resb = [n for n in a if n % 3 == 0]  # print dividble by 3
resoo = [n for n in a if n % 2 != 0]  # print odd

labeled_wl = [(w, "... is a longer word" if len(w) >= 5 else ".. is a shorter word") for w in words]
labeled_n= [f"{n} is {'even' if n % 2 == 0 else 'odd'}" for n in a]  #label them !!!
labeled_turnUpper_ifLower = [w.upper() if w.islower() else w for w in words]


print(resa)
print(resb)
print(resoo)
print(labeled_wl)
print(labeled_n)
print(labeled_turnUpper_ifLower)

print("-------------------------------------------\n")
names = ["Alex", "Kim", "Jordan"]
courses = ["CIS 247", "Math 120", "CS 101", "Chem"]

name_length = [f"Length for word {n} is {len(n)}" for n in names]
c_courses = [f"{n}... starts with C" for n in courses if n.startswith("C")]

print (name_length)
print (c_courses)

print("-------------------------------------------\n")
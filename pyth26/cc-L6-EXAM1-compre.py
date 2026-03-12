

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
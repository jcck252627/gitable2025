import random
a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
fruits = ["apple", "banana", "cherry"]
colors = ["red", "green", "blue"]

for f in fruits:
    print(f"The fruit is: {f}")

for i in  range (len(a)):
    print(f"Index {i} has value {a[i]}")
i=0
while i < len(colors):
    print(f"The magic color is:  {colors[i]}")
    i += 1

age = 20
if age < 13:
    print("Child")
elif age < 18:
    print("Teenager")
else:
    print(f"The age of {age} is ....Adult")


word = "Hello How Are You My Dear"
for ch in word:
    print(ch, end = ' ')

for n in range(0, 550, 50):
    print("Number:", n)

animals = ["dog", "cat", "bird", "lion","wolf","tutle","hawk","ox","dolphin"]
for index, animal in enumerate(animals):
    print(index, animal)    

print(f"A random number was picked between 1-2,000 :  {random.randint(1, 2000):,}")  
print(f"A random animal was chosen: {random.choice(animals)}")  
myList = [123, 123, 1.23]
print(len(myList)) # prints 3
myList.append("555")
print(len(myList)) 


name = 'Jonathan'
print(name[0:])
print(name[:2])

print(name[2:3])
print(name[3:6])

string1 = "Cypress "
string2 = "College"
tt=string1 + string2
print(tt)


name = "Jonathan"
name2 = name
name = "Bob"
print(name2)
print(name)



state = "California"
kkkk=state.find("for")
print(kkkk)
state.find("for") # Returns 4
state.find("a") # Returns 1
state.find("xyz") # Returns -1


state = "California"
ttttt= state.replace("al", "b")
print(ttttt)

str = "HelloHelloHello"
newStr = str.replace("Hello", "Hi") # newStr references a string with 'HiHiHi'
print(newStr)

str = "1234"
print(str.isdigit()) # prints True
str = "123b4"
print(str.isdigit()) # prints 

str = "Hello"
print(str.upper()) # prints HELLO

str = "Hello"
print(str.lower()) # prints hello

myList = [123, 'a string', 1.23]
myList[1] = "Hello"
print(myList)

myList.append('GoodBye')
print(myList)

myList.append('HowRU')
print(myList)

myList.pop()
print(myList)

myList.pop(0)
print(myList)

myList2 = [123, 495, -11.23,34556]
myList2.sort()
print(myList2)

num_sales = 50
print("You have made num_sales sales today")

myList = [123, 4444, 1.23]
print(myList)
myList.append("Hello")
print(myList)

name = "Jonathan"
print(f'Hello {name}!')
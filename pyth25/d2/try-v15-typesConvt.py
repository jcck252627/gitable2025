
length_of_this=len(str(1233445))
print(length_of_this)

# find type of data
print(type("hello"))
print(type(1.2442321))
print(type(13433677))
print(type(True))

print(" ************type conversion commands ****************")

print(int("23423") + int("3556"))

#run this without any error
# print("number of letter in your name: " + len(input("enter your name "))
# print("number of letter in your name: " + len(input("enter your name "))
name = input("enter your name: ")
namelen_int = len(name)
print(type(namelen_int))
namelen_str = str(int(len(name)))
print(type(namelen_str))
print("the number of characters in your name is: "+namelen_str)


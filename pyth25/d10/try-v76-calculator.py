def add(n1, n2):
    return n1+n2


def subtract(n1,n2):
    return n1-n2

def multiply(n1,n2):
    return n1*n2

def divide(n1, n2):
    return n1/n2

math_operation = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide

}


while True:
    try:
        n1 = float(input("Please Enter your first number: "))
        break
    except ValueError:
        print("Please ensure you enter a number...")


print("Good")
print("Please Enter a math operation to be performed  ")
print('"+" for addition ')
print('"-" for subtraction ')
print('"*" for multiplication ')
print('"/" for division ')


while True:
    operation = input("------------>  ")
    if operation in ["+", "-", "*", "/"]:
        break
    else:
        print("You have entered an invalid operation, please try again.")
print("Valid operation selected:", operation)

while True:
    try:
        n2 = float(input("Please Enter your second number: "))
        break
    except ValueError:
        print("Please ensure you enter a number ...")


anwser=print("The operation "+str(n1)+" "+operation+" "+str(n2)+" is equal to: "+ str(math_operation[operation](n1,n2)))




# print(math_operation["*"](4,8))

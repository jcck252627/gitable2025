def get_validated_num1():
    while True:
        num1 = input("Please enter the 1st number (whole number only): ")
        if num1.isdigit():
            return int(num1)
        print("Invalid input. Please enter a whole number for 1st number only.")

def get_validated_num2():
    while True:
        num2 = input("Please enter the 2nd number (whole number only): ")
        if num2.isdigit():
            return int(num2)
        print("Invalid input. Please enter a whole number for 2nd number only.")        

def get_validated_calculator_option():
    while True:
        option = input("Choose an operation — '0' To ADD these 2 numbers ... '1' To Mulitply these 2 numbers ... or type 'Stop' to EXIT this program:  ").strip().lower()
        if option == "0":
            return int(option)
        elif option =="1":
            return int(option)
        elif option == "stop":
            print("You have entered 'stop', the program will END now, thank you")
            import sys
            sys.exit(0)
        else:
            print("Invalid input. Please enter '0', '1' or 'stop' only ......")        


user_choice = 100
n1 = 100
n2 = 100
n1 = get_validated_num1()
n2 = get_validated_num2()
print(n1)
print(n2)
user_choice = get_validated_calculator_option()
print(user_choice)
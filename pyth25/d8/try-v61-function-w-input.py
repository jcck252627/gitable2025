def greet(name):
    print(f"Hello {name} ")
    print(f"How are you {name}")
    print(f"Isn't the weather nice {name} ?")



name = input("Enter your name:  ")
greet(name)


def greet():
    print("Hello Angela")
    print("How do you do Jack Bauer?")
    print("Isn't the weather nice?")


greet()


# Function that allows for inputs
def greet_with_name(name):
    print(f"Hello {name}")
    print(f"How do you do {name}?")


greet_with_name("Billie")

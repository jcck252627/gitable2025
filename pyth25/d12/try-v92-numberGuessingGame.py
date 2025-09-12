import random
import art

def pick_number():
    return random.randint(1,100)

#def compare():


number_picked= pick_number()
print(f"The number picked by computer is:  {number_picked}")

number_guessed=int(input("Pick a number between 1 and 100 you want to guess:  "))
print(f"The number player picked is {number_guessed}")



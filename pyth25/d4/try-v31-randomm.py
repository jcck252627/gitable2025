import random
import my_module   # import module reference in my module file ....


number=random.randint(1,100)
print(number)

# referred the defined value in my module file
print(my_module.my_num3)
print(my_module.my_num4)
print(my_module.my_num5)


# how to create random floating point number
# generating random floats
# randomizing floats between 0.0 and 10 ... if 0 to 1 ... then no *number
random_float = random.random() *10
print(random_float)

# Generate a random float between 1.5 and 5.5
random_number = random.uniform(1.5, 5.5)
print(f"Random number between 1.5 and 5.5: {random_number}")

# note that the random generation would only go up to 4.999999999


#now play the head or tail program
print("********************************************")
print("Welcome to the random coin toss game ")
flip_coin = random.randint(0,1)
if flip_coin == 0:
    print("It's a Tail !!")
else:
    print("It's a Head !!")





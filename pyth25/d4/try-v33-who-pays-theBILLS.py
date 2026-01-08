# use knowledge of randomization and list in python , write code to see who gets to pay the bil
import random

friends=["John","Meggie","Peter","Bob","Jody","Chris","Kara"]
# doc to look for built function in random module
print(random.choice(friends))

# using basic random function to generate random number to put into list index
pick=random.randint(0,6)
print(friends[pick])



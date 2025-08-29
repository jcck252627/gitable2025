
def my_function():
    print("Hello World!")


n = 0
while n < 4:
    my_function()
    n += 1

print("--------------------------------")
# robot hurdle example where we needed to jump 6 times
print("robot hurdles example to jump 6 times")
hurdles=6

while hurdles > 0:
    hurdles -= 1
    print("jump")


    # use the FOR loop ... when we need to iterate through some condition within a range
    # use the WHILE loop ... when we have a specific condition we want to meet  ... more chance of endless loop since no fixed range
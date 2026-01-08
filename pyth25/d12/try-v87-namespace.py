enemies = 1
strength = 100 # globally scoped value

def increase_enemies():
    enemies = 2 # locally scoped value
    print(f"enemies inside function: {enemies}")
    print(f"Strength count inside function: {strength}")

increase_enemies()
print(f"enemies outside function: {enemies}")
print(f"Strength count outside function: {strength}")

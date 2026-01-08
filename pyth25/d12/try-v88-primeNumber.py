def is_prime(num):
    if num <= 1:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    for i in range(3, int(num**0.5) + 1, 2):
        if num % i == 0:
            return False
    return True



input = 73

if is_prime(input) == "True":
    print(f"The number {input} IS a prime number")
else:
    print(f"The number {input} IS NOT a prime number")

f = 1
for i in range(2, 18):
 f = f * i
 print(f"f now is : {f:,.2f}")
print(f"7!= {f:,.2f}")




end_loop = False
nums = []
print("Enter as many numbers as you want. Enter 'quit' to stop")
while True:
 num = input("Enter the next number: ")
 if num == 'quit':
    break
 else:
    nums.append(num)
print("You entered the following values")
for val in nums:
    print("store #",val, end=' ...')
    print("Store ID ", val)
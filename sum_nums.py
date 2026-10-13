n = int(input("Enter a number: "))

running_sum = 0
for i in range(1,n + 1):
    running_sum += i

sum_gauss = n * (n + 1) // 2  

print(f"Running sum (loop): {running_sum}")
print(f"Gauss sum (loop): {sum_gauss}")

if running_sum == sum_gauss:
    print("My running sum code works correctly")
else:
    print("My running sum code failed badly")
    
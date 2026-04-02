num = int(input("Enter the number: "))

n = num
factorial = 1

while n > 0:
    factorial *= n
    n -= 1

print(f"Factorial of {num} is {factorial}")
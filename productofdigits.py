num = int(input("Enter the number to find product of digits:"))

n = num
product = 1

while n > 0:
    temp = n % 10
    product *= temp
    n = n//10


print(f"The product of digits of {num}: {product}")

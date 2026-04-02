num1 = int(input("Enter 1st number: "))
num2 = int(input("Enter 2nd number: "))

product = 1

for i in range(num1, num2 + 1):
    product *= i

print(f"Product of numbers between {num1} and {num2} is {product}")
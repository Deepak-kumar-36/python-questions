num1 = int(input("Enter 1st number: "))
num2 = int(input("Enter 2nd number: "))

count = 0

for i in range(num1, num2 + 1):
    count += 1

print(f"Total Numbers between {num1} and {num2} is {count}")
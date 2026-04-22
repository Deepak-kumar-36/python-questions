num = int(input("Enter the number to count number of digits:"))

n = num
count = 0

while n > 0:
    n = n//10
    count += 1

print(f"The number of digits in {num}: {count}")

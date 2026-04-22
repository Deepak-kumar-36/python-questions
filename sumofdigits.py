num = int(input("Enter the number to find sum of digits:"))

n = num
sum = 0

while n > 0:
    temp = n % 10
    sum += temp
    n = n//10


print(f"The sum of digits of {num}: {sum}")

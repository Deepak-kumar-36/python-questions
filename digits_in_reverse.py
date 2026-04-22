num = int(input("Enter the number to print it in reverse order:"))

n = num

print(f"{num} in reverse order:", end = " ")

while n > 0:
    temp = n % 10
    print(temp, end = "")

    n = n//10

print()

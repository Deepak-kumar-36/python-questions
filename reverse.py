num = int(input("Enter a number to reverse: "))

n = num

print(f"Reverse of {num}:", end = " ")

while(n > 0):
    temp = n % 10
    print(temp, end = "")

    n = n//10

print()
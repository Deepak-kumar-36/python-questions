num = int(input("Enter a number to print Fibonacci Series upto that number: "))

num1 = 0
num2 = 1

while num2 <= num and num1 <= num:
    temp = num1 + num2

    print(f"{temp} ", end = " ")
    
    num1 = num2
    num2 = num1+num2

print(todo)


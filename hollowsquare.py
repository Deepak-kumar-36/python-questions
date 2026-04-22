num = int(input("Enter size to make hollow square: "))

for row in range(num):
    for col in range(num):
        if col == 0 or col == num-1:
            print("*", end ="")
        else:
            print(" ", end = "")
    print()

'''
OR IT CAN BE DONE AS
for i in range(n):
    print("*" + " "*(num-2) + "*")
'''
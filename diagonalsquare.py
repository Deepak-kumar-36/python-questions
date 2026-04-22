num = int(input("Enter size to make square with diagonal (*): "))

for row in range(num):
    for col in range(num):
        if col == 0 or col == num-1:
            print("*", end ="")
        
        

    print()

rows = int(input("Enter number of rows: ")) 
for a in range(rows):
    for b in range(rows * 2 - 1):
        if b < rows - a - 1:
            print(" " , end="")
        elif b <= rows + a - 1:
            print("*" , end="")
    print()
for i in range(rows-1 , 0 , -1):
    for m in range(rows - i):
        print(" " , end="")
    for j in range(2 * i - 1):
        print("*" , end= "")
    
    print()
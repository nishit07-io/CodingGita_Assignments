# M E T H O D  -  1

rows = int(input("Enter number of rows: "))
for i in range(1 , rows + 1):
    for j in range(rows - i , 0 , -1):
        print("-" , end=" ")
    for m in range(2*i-1):
        print("*" , end=" ")
    print()

# M E T H O D  -  2

for a in range(rows):
    for b in range(rows * 2 - 1):
        if b < rows - a - 1:
            print("-" , end=" ")
        elif b <= rows + a - 1:
            print("*" , end=" ")
    print()
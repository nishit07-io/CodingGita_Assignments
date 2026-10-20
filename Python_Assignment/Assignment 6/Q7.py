rows = int(input("Enter number of rows: "))
for i in range(rows):
    for j in range(i):
        print(chr(65 + j) , end=" ")
    print()
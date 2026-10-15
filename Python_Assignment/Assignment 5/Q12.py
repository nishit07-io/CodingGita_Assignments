n = int(input("Enter ending number: "))
ec = 0
oc = 0
for i in range(1 , n + 1):
    if i % 2 == 0:
        ec += 1
    else:
        oc += 1
print("Even" , ec , "odd" , oc)
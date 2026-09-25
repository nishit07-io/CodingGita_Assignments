num = int(input())

if num < 10:
    print("One Digit")
elif num < 100:
    print("Two Digits")
elif num < 1000:
    print("Three Digits")
else:
    print("Four or More Digits")

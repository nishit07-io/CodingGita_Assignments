s = input("Enter a string: ")
result = ""
for ch in s:
    if ch.lower() not in "aeiou":
        result += ch
print(result)

character = input()

print(f"Character: {character}")
print(f"Code: {ord(character)}")
print(f"Previous: {chr(ord(character) - 1)}")
print(f"Next: {chr(ord(character) + 1)}")
email = input()
at_present = "@" in email
username, domain = email.split("@")

print(f"@ Present: {at_present}")
print(f"Username: {username}")
print(f"Domain: {domain}")
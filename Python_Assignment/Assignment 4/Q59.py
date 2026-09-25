email = input()
domain = email.split("@")[1]

if domain == "gmail.com":
	print("Gmail User")
else:
	print("Other Email Provider")

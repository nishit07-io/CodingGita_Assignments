username = input("Enter username: ")
password = input("Enter password: ")

if username == "admin":
	if password == "admin123":
		print("Login Successful")
	else:
		print("Wrong Password")
else:
	print("Invalid Username")

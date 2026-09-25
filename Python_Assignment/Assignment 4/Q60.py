full_name = input().strip().split()
username = f"{full_name[0]}.{full_name[-1]}"

if "." in username:
	print("Valid Username Format")
else:
	print("Invalid Username Format")

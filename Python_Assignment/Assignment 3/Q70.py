full_name = input()
name_parts = full_name.split()
first_name = name_parts[0]
last_name = name_parts[-1]

print(
	f"Original: {full_name}\n"
	f"First Name: {first_name}\n"
	f"Last Name: {last_name}\n"
	f"First Name (Upper Part): {first_name[:3].upper()}\n"
	f"Last Name (Lower Part): {last_name[1:].lower()}\n"
	f"Full Name Reversed: {full_name[::-1]}"
)

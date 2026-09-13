student_id = input().strip()
parts = student_id.split("-")

degree = parts[0]
batch = parts[1]
branch = parts[2]
roll = parts[3][:]

print(f"Degree: {degree}")
print(f"Batch: {batch}")
print(f"Branch: {branch}")
print(f"Roll: {roll}")
print(f"Code: {degree}/{branch}/{roll}")

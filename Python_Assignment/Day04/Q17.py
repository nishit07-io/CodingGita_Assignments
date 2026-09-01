total_students = 23
students_per_group = 5

complete_groups = total_students // students_per_group
remaining_students = total_students % students_per_group

print("Total students:", total_students)
print("Students per group:", students_per_group)
print("Number of complete groups:", complete_groups)
print("Remaining students:",  remaining_students)
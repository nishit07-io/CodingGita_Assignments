total_seconds = 7384

hours = total_seconds // 3600
minutes = (total_seconds % 3600) // 60
seconds = total_seconds % 60

print(hours, "hours,", minutes, "minutes,", seconds, "seconds")
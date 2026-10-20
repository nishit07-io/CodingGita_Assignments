n = int(input('Number count: '))
previous = None
current = None
peaks = 0
for i in range(n):
    following = int(input('Number: '))
    if previous is not None and current is not None:
        if current > previous and current > following:
            peaks += 1
    previous, current = (current, following)
print(peaks)
days = int(input('Days: '))
stations = int(input('Stations: '))
for i in range(1, days + 1):
    total = 0
    for j in range(1, stations + 1):
        total += float(input(f'Day {i}, station {j}: '))
    print(f'Day {i} total: {total:g}')

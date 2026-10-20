s = input('Number: ')
repeated = False
for i in range(len(s)):
    for j in range(i + 1, len(s)):
        for k in range(len(s)):
            for m in range(k + 1, len(s)):
                if (i, j) != (k, m) and int(s[i]) + int(s[j]) == int(s[k]) + int(s[m]):
                    repeated = True
if repeated:
    print('Repeated pair sums exist')
else:
    print('No repeated pair sums')
t = int(input())
for _ in range(0, t):
    n = input()
    a = list(map(int, n))
    sumDigit = str(sum(a, 0))

    if len(sumDigit) > 1 and sumDigit == sumDigit[::-1]:
        print('YES')
    else:
        print('NO')

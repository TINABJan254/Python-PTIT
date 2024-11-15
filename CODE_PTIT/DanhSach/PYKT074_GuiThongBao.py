for _ in range(0, int(input())):
    s = input().strip()
    if len(s) < 100:
        print(s)
    else:
        k = 100
        while s[k] != ' ':
            k -= 1
        print(s[:k].strip())
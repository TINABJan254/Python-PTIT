t = int(input())

for _ in range(t):
    n = input()
    s1 = n[0] + n[1]
    s2 = n[len(n) - 2] + n[len(n) - 1]
    if s1 == s2:
        print("YES")
    else:
        print("NO")
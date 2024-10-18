n, m = map(int, input().split())
a = set(map(int, input().split()))
b = set(map(int, input().split()))

#sortd(x) : x is iterable, return list
s1 = sorted(a.intersection(b))
s2 = sorted(a - b)
s3 = sorted(b - a)

print(*s1)
print(*s2)
print(*s3)


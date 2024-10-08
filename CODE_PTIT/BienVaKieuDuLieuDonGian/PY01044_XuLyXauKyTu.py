a = set(input().lower().split())
b = set(input().lower().split())

u = list(a.union(b))
its = list(a.intersection(b))

u.sort()
its.sort()

print(*u)
print(*its)
# union, intersection chỉ áp dụng trên set


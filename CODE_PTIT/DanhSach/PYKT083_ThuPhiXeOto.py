d = {
    ("Xe_con", "5")     : 10000,
    ("Xe_con", "7")     : 15000,
    ("Xe_tai", "2")     : 20000,
    ("Xe_khach", "29")  : 50000,
    ("Xe_khach", "45")  : 70000
}

n = int(input())
res = {}
for i in range(0, n):
    a = list(input().split())
    if a[3] == 'IN':
        date  = a[4]
        fee = d[(a[1], a[2])]
        if (date in res):
            res[date] += fee
        else:
            res[date] = fee

for x in res:
    print(x, ": ", res[x], sep = "")

import json


# main
t = int(input())
for _ in range(t):
    line = input()
    a = json.loads(line)

    l = []
    s = 0
    cnt = 0
    for x in a:
        if str(a[x]).isnumeric():
            l.append(x)
            s += a[x]
        if str(a[x]).isalpha():
            cnt += 1
    
    print(f'({l}, {s}, {cnt})')

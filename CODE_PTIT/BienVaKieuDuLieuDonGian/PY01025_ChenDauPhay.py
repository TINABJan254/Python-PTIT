s = input()
res = ''
cnt = 1
for i in range(-1, (len(s) + 1)*(-1), -1):
    if cnt == 3 and i != len(s)*-1:
        res = ',' + s[i] + res
        cnt = 1
    else:
        res = s[i] + res
        cnt += 1
print(res)
s = input()
cnt = 0
a = list(s)

for i in range(-1, len(a) * -1 - 1, -1):
    cnt += 1
    if cnt == 3:
        
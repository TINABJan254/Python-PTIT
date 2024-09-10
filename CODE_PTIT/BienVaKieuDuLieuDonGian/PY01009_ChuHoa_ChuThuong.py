s = input()
cntL, cntU = 0, 0
for x in s:
    if x.islower(): cntL += 1
    else: cntU += 1

if cntL >= cntU: print(s.lower())
else: print(s.upper())
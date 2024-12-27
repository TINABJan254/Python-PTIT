s = input()
while (len(s) != 1):
    tmp = int(s[:len(s)//2]) + int(s[len(s)//2:])
    s = str(tmp)
    print(s)
from functools import cmp_to_key


class SinhVien:
    def __init__(self, ten, ac, sub):
        self.ten = ten
        self.ac = ac
        self.sub = sub
    
    def __str__(self):
        return f'{self.ten} {self.ac} {self.sub}'

def cmp(a, b):
    if a.ac != b.ac: return b.ac - a.ac
    return a.sub - b.sub

# main
n = int(input())
a = []
for _ in range(n):
    ten = input()
    ac, sub = map(int, input().split())
    a.append(SinhVien(ten, ac, sub))

a.sort(key = cmp_to_key(cmp))
for x in a:
    print(x)
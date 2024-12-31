from functools import cmp_to_key


class GameThu:
    def __init__(self, id, ten, gioVao, gioRa):
        self.id = id
        self.ten = ten
        self.gioVao = gioVao
        self.gioRa = gioRa
    
    def gioChoi(self):
        h1, m1 = map(int, self.gioVao.split(':'))
        h2, m2 = map(int, self.gioRa.split(':'))
        h = h2 - h1
        m = m2 - m1
        if m < 0:
            m += 60
            h -= 1
        return h

    def phutChoi(self):
        h1, m1 = map(int, self.gioVao.split(':'))
        h2, m2 = map(int, self.gioRa.split(':'))
        m = m2 - m1
        if m < 0:
            m += 60
        return m
    
    def __str__(self):
        return self.id + " " + self.ten + " " + f'{self.gioChoi()} gio {self.phutChoi()} phut'

def cmp(a, b):
    if a.gioChoi() > b.gioChoi():
        return -1
    if a.gioChoi() < b.gioChoi():
        return 1
    if a.phutChoi() > b.phutChoi():
        return -1
    return 1

#main
n = int(input())
a = []
for i in range(n):
    a.append(GameThu(input(), input(), input(), input()))

a.sort(key = cmp_to_key(cmp))

for x in a:
    print(x)
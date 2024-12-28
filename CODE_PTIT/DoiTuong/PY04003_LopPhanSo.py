import math

class PhanSo:
    def __init__(self, tu, mau):
        self.tu = tu
        self.mau = mau
    
    def rutGon(self):
        uc = math.gcd(self.tu, self.mau)
        self.tu //= uc
        self.mau //= uc

    def __str__(self):
        return f"{self.tu}/{self.mau}" 

#main
a, b = map(int, input().split())
ps = PhanSo(a, b)
ps.rutGon()
print(ps)
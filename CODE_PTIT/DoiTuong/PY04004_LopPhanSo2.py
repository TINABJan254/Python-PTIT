import math

class PhanSo:
    def __init__(self, tu, mau):
        self.tu = tu
        self.mau = mau
    
    def rutGon(self):
        uc = math.gcd(self.tu, self.mau)
        self.tu //= uc
        self.mau //= uc

    def cong(self, other):
        res = PhanSo(0, 0)
        res.tu = self.tu * other.mau + self.mau * other.tu
        res.mau = self.mau * other.mau
        return res

    def __str__(self):
        return f"{self.tu}/{self.mau}" 

#main
arr = list(map(int, input().split()))
res = PhanSo(arr[0], arr[1]).cong(PhanSo(arr[2], arr[3]))
res.rutGon()
print(res)
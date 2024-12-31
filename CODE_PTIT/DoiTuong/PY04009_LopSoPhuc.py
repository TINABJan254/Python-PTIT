class SoPhuc:
    def __init__(self, thuc, ao):
        self.thuc = thuc
        self.ao = ao 
    
    def __add__(self, other):
        return SoPhuc(self.thuc + other.thuc, self.ao + other.ao)
    
    def __mul__(self, other):
        return SoPhuc(self.thuc * other.thuc - self.ao * other.ao, self.thuc * other.ao + self.ao * other.thuc)

    def __pow__(self, o):
        res = self
        for _ in range(1, o):
            res = res * self
        return res

    def __str__(self):
        res = str(self.thuc)
        if self.ao < 0:
            res += ' - '
        else:
            res += ' + '
        res += str(abs(self.ao)) + 'i'
        return res

#main
for _ in range(0, int(input())):
    a = list(map(int, input().split()))
    x = SoPhuc(a[0], a[1])
    y = SoPhuc(a[2], a[3])
    z = (x + y) * x
    t = (x + y) ** 2
    print(f"{z}, {t}")
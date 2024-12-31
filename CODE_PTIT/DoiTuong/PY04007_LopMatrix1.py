class Matrix:
    def __init__(self, a):
        self.a = a

    def transpose(self):
        return Matrix([[row[i] for row in self.a] for i in range(len(a[0]))])

    def mul(self, other):
        res = [[0 for _ in range(len(other.a[0]))] for _ in range(len(self.a))]
        for i in range(0, len(self.a)):
            for j in range(0, len(self.a)):
                for k in range(0, len(self.a[0])):
                    res[i][j] += self.a[i][k] * other.a[k][j]
        return Matrix(res)

    def __str__(self):
        res = ''
        for x in self.a:
            res += ' '.join(map(str, x)) + '\n'
        return res.strip()

#main
for _ in range(0, int(input())):
    n, m = map(int, input().split())
    a = []
    for i in range(0, n):
        a.append(list(map(int, input().split())))
    
    mt1 = Matrix(a)
    res = mt1.mul(mt1.transpose())
    print(res)
    
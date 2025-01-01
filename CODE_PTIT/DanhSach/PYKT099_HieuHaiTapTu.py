with open('DanhSach/DATA1.in', 'r') as fo:
    a = [word.lower() for word in fo.read().strip().split()]

with open('DanhSach/DATA2.in', 'r') as fo:
    b = [word.lower() for word in fo.read().strip().split()]

for x in sorted(set(a).difference(set(b))):
    print(x, end = ' ')
print()
for x in sorted(set(b) - set(a)):
    print(x, end = ' ')
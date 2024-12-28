class Rectangle:
    def __init__(self, w, h, c):
        self.w = w
        self.h = h
        self.c = c
    
    def perimeter(self):
        return (self.w + self.h) * 2

    def area(self):
        return self.w * self.h

    def color(self):
        return self.c[:1].upper() + self.c[1:].lower()

arr = input().split()
if int(arr[0]) > 0 and int(arr[1]) > 0:
    r = Rectangle(int(arr[0]), int(arr[1]), str(arr[2]))
    print('{} {} {}'.format(r.perimeter(), r.area(), r.color()))
else:
    print('INVALID')
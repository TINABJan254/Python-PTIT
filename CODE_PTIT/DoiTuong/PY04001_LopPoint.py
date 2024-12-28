from decimal import Decimal
import math

class Point:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y
    def distance(self, other):
        dis = math.sqrt(pow(self.__x - other.__x, 2) + pow(self.__y - other.__y, 2))
        return f"{dis:.4f}"


if __name__ == '__main__':
    t = int(input())
    while t > 0:
        arr = input().split()
        p1 = Point(Decimal(arr[0]), Decimal(arr[1]))
        p2 = Point(Decimal(arr[2]), Decimal(arr[3]))
        print(p1.distance(p2))
        t -= 1
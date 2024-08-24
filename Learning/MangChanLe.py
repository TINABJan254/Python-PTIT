#đọc mảng không biết trước số lượng phần tử
import math
import sys

if __name__ == '__main__':
    a = []
    for s in sys.stdin:
        a += list(map(int, s.split()))
    chan, le = 0, 0
    for x in a:
        if x % 2 == 0: chan += 1
        else: le += 1
    if chan == le: print('CHAN LE')
    elif chan > le: print('CHAN')
    else: print('LE')
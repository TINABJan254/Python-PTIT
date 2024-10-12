final = False
n, k = 0, 0
x = []
a = []

def init():
    global x, n, k
    x = [0]*n
    for i in range(0, k):
        x[i] = i

def display():
    global a, x, k
    for i in range(0, k):
        print(a[x[i]], end = ' ')
    print()

def genNext():
    global final, n, k, x
    i = k - 1
    while i >= 0 and x[i] == n - k + i:
        i -= 1
    
    if i < 0:
        final = True
    else:
        x[i] += 1
        for j in range(i + 1, k):
            x[j] = x[j - 1] + 1 

if __name__ == '__main__':
    n, k = map(int, input().split())
    a = list(set(map(str, input().split())))
    a.sort()
    n = len(a)
    init()
    
    while not final:
        display()
        genNext()

    


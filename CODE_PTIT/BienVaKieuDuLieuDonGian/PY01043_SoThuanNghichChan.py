def check(n):
    if n != n[::-1]:
        return False
    
    for c in n:
        if c not in ['0', '2', '4', '6', '8']:
            return False
    return len(n) % 2 == 0
    

if __name__ == '__main__':
    t = int(input())
    for _ in range(0, t):
        n = int(input())
        for i in range(22, n, 2):
            if check(str(i)):
                print(i, end = ' ')
        print()


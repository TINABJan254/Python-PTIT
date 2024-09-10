def check(n):
    if len(n) < 3:
        return False
    ok = False
    for i in range(1, len(n)):
        if ok : break
        left_ok = True
        right_ok = True
        #check 0->i
        for L in range(0, i):
            if n[L] >= n[L + 1]: 
                left_ok = False
                break
        
        #check i->len(s)
        for R in range(i, len(n) - 1):
            if n[R] <= n[R + 1]: 
                right_ok = False
                break
        
        #
        ok = left_ok and right_ok
    return ok

if __name__ == '__main__':
    t = int(input())
    for _ in range(0, t):
        n = input()
        if check(n):
            print("YES")
        else:
            print("NO")
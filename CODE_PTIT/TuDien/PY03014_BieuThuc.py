import math


# main
for _ in range(int(input())):
    a = [x for x in input() if x == '(' or x == ')']

    stack = []
    cnt = 0
    res = []
    for i in range(0, len(a)):
        if a[i] == '(':
            cnt += 1
            res.append(cnt)
            stack.append(i)
        else:
            res.append(res[stack[-1]])
            stack.pop()
    
    for x in res:
        print(x, end = ' ')
    print()

'''
2
(a + (b *c) ) + (d/e)
( ( () ) ( () ) )
'''
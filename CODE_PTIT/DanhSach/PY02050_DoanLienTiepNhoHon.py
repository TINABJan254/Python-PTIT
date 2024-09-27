for _ in range(0, int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    
    d = [0] * n
    st = []
    for i in range(0, n):
        while st and a[i] >= a[st[-1]]:
            st.pop()
        if not st:
            d[i] = i + 1
        else:
            d[i] = i - st[-1]
        st.append(i)
    
    print(*d)
    


for _ in range(0, int(input())): 
    print('YES') if sum(list(map(int, input()))) % 3 == 0 else print('NO')
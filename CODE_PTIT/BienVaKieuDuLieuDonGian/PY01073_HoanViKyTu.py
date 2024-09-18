from itertools import permutations

if __name__ == '__main__':
    n = input()
    perm = permutations(n)
    for i in perm:
        for j in i:
            print(j, end = '')
        print()
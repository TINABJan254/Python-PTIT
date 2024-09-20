s1, s2 = input(), input()
p = int(input())
new_str = s1[:p-1] + s2 + s1[p-1:]
print(new_str)

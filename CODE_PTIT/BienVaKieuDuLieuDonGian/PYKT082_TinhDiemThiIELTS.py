import math

def cd(n):
    if n <= 4: return 2.5
    if n <= 6: return 3.0
    if n <= 9: return 3.5
    if n <= 12: return 4.0
    if n <= 15: return 4.5
    if n <= 19: return 5.0
    if n <= 22: return 5.5
    if n <= 26: return 6.0
    if n <= 29: return 6.5
    if n <= 32: return 7.0
    if n <= 34: return 7.5
    if n <= 36: return 8.0    
    if n <= 38: return 8.5
    if n <= 40: return 9.0
    
if __name__ == '__main__':
    for _ in range(0, int(input())):
        a = list(input().split())
        res = (cd(int(a[0])) + cd(int(a[1])) + float(a[2]) + float(a[3]) ) / 4
        if res - math.floor(res) < 0.25:
            res = math.floor(res)
        elif res - math.floor(res) >= 0.25 and res - math.floor(res) < 0.75:
            res = math.floor(res) + 0.5
        else: res = math.ceil(res)
        print(f"{res:.1f}")

         
        



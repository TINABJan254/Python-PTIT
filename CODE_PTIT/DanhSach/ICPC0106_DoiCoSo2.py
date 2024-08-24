import math

if __name__ == '__main__':
    t = int(input())
    for _ in range(0, t):
        n = int(input())
        s = input()
        x = int(s, 2)
        
        if n == 2:
            print(s)
        elif n == 4:
            res = ''
            while x > 0:
                res = str(x % 4) + res
                x //= 4
            print(res)
        elif n == 8:
            #có thể dùng cách chia như hệ 4
            #python có hỗ trợ hàm oct(x) chuyển x từ hệ thập phân sang hệ 8, tuy nhiên output sẽ có 0o ở đầu, vd 0o45
            res = str(oct(x))[2:]
            print(res)
        elif n == 16:
            #tương tự hệ 8, có thể dùng chia hoặc hàm hỗ trợ output là 0x5FA
            res = str(hex(x))[2:]
            print(res.upper())

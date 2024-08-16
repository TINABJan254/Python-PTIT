def sayHi(n):
    if n == 1:
        return
    else:
        print("Hello guys")
        n -= 1
        sayHi(n)

if __name__ == "__main__":
    print("hello world")
    sayHi(5)
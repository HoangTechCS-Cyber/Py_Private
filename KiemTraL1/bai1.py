def fact(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def calc(x, n):
    result = 1
    for i in range(1, n + 1):
        result += (x ** i) / fact(i)
    return result

x, n = map(float, input("Nhập x, n: ").split())
n = int(n) 

print("Giá trị xấp xỉ của e^x:", calc(x, n))

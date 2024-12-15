a = [int(input()) for i in range(int(input("nhap k: ")))]
n, m = map(int, input().split())
if len(a)//n == m:
    d = [[int(input(f"d[{i}][{j}] = ")) for j in range(m)] for i in range(n)]
    print(d)
else:
    print("Not")

#1
n = int(input("Nhập số lượng phần tử cho mảng a: "))
a = []
for i in range(n):
    a.append(int(input(f"Nhập phần tử thứ {i + 1}: ")))

a.sort()
print("Mảng a sau khi sắp xếp tăng dần:", a)
#2
max_val = max(a)
min_val = min(a)
first_index = next((index for index, val in enumerate(a) if val % 2 == 0), None)
contains_three = 3 in a
print("Vị trí số chẵn đầu tiên:", first_index if first_index is not None else "Không có")
print("Mảng có chứa số 3:", "Có" if contains_three else "Không")
#3
k = int(input("Nhập vị trí k : "))
new_element = int(input("Nhập phần tử mới: "))
a.insert(k, new_element)

a = [val for val in a if val % 2 != 0]
print("Mảng sau khi chèn và xóa các số chẵn:", a)

m = int(input("Nhập số lượng phần tử cho mảng b: "))
b = []
for i in range(m):
    b.append(int(input(f"Nhập phần tử thứ {i + 1}: ")))

b_doubled = b * 2
b_doubled.reverse()

c = a + b_doubled
print("Mảng c sau khi nối ghép:", c)
# Khai báo list
my_list = [1, 2, 3, 4, 5]
mixed_list = [1, "Hello", 3.14, True]

# Truy cập phần tử
print("Phần tử đầu tiên trong my_list:", my_list[0])  # In ra 1
print("Phần tử thứ hai trong mixed_list:", mixed_list[1])  # In ra "Hello"

# Thay đổi giá trị phần tử
my_list[2] = 10  # Đổi giá trị phần tử thứ 3 thành 10
print("my_list sau khi thay đổi:", my_list)

# Thêm phần tử
my_list.append(6)
print("my_list sau khi thêm phần tử 6:", my_list)
my_list.insert(2, 15)  # Chèn số 15 vào vị trí thứ 3co
print("my_list sau khi chèn 15 vào vị trí thứ 3:", my_list)

# Xóa phần tử
my_list.remove(3)  # Xóa phần tử có giá trị là 3
print("my_list sau khi xóa phần tử 3:", my_list)
popped_item = my_list.pop(1)  # Xóa phần tử ở vị trí thứ 2
print("Phần tử bị xóa:", popped_item)
print("my_list sau khi pop phần tử thứ 2:", my_list)
my_list.clear()  # Xóa toàn bộ phần tử
print("my_list sau khi clear:", my_list)

# Tạo lại danh sách để minh họa tiếp
my_list = [3, 1, 4, 1, 5, 9]

# Duyệt qua các phần tử
print("Duyệt qua các phần tử trong my_list:")
for item in my_list:
    print(item)

# Độ dài của list
print("Độ dài của my_list:", len(my_list))

# Sắp xếp và đảo ngược
my_list.sort()  # Sắp xếp theo thứ tự tăng dần
print("my_list sau khi sắp xếp:", my_list)
my_list.reverse()  # Đảo ngược thứ tự
print("my_list sau khi đảo ngược:", my_list)

# Ví dụ minh họa cuối cùng
numbers = [3, 1, 4, 1, 5, 9]
numbers.append(2)
print("numbers sau khi thêm 2:", numbers)
numbers.sort()
print("numbers sau khi sắp xếp:", numbers)


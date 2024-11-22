# Khởi tạo tuple bằng ngoặc tròn, không thay đổi giá trị được
a = (1, 3, 2, 4, 5)
b = ("Hoa", [1, 2, 3], "Hồng", (2, 2))
# Đóng gói nhiều giá trị vào một tuple
info = ("Alice", 25, "Developer")
print(info)  # output: ("Alice", 25, "Developer")

# Mở gói tuple thành các biến
name, age, job = info
print(name)   # Alice
print(age)    # 25
print(job)    # Developer

# Built-in methods for tuple
# Đếm số lượng phần tử xuất hiện trong tuple
count_of_Alice = info.count("Alice")
print(f"Số lần 'Alice' xuất hiện trong tuple: {count_of_Alice}")  # Output: 1

# Tìm vị trí đầu tiên của một phần tử trong tuple
index_of_25 = info.index(25)
print(f"Vị trí của 25 trong tuple: {index_of_25}")  # Output: 1

def test(n, data_type):
    import time
    if data_type == "list":
        _start = time.time()
        a = [i for i in range(n)]
        end_time = time.time()
    elif data_type == "tuple":
        _start = time.time()
        a = tuple(i for i in range(n))
        end_time = time.time()
    else:
        print("Loại dữ liệu không hợp lệ. Vui lòng chọn 'list' hoặc 'tuple'.")
        return
    print(f"Time to create a {data_type}: {end_time - _start} seconds")

# Sử dụng số nguyên cho n thay vì chuỗi
n = 10000000  # 10 triệu để tránh quá tải bộ nhớ

test(n, "list")
test(n, "tuple")

#Set
#khoi tao set 
fruits = {"apple", "banana", "cherry"}
print(fruits)
#khoi tao mot set rong
name_set = set()
#them phan tu vao cuoi  
fruits.add("orange")
print(fruits)
#them nhieu phan tu 
fruits.update(["mango", "grape"])
print(fruits)
#xoa phan tu
#xoa phan tu neu no ton tai trong set 
fruits.remove("banana") #neu trong set khong ton tai banana, lenh se bao loi KeyError
print(fruits) 
#Xoa phan tu ma khong gay loi neu khong ton tai 
fruits.discard("apple")


#Dictionary: la mot ctdl mà mỗi mục (item) là một cặp key : value.
#khoi tao mot dict rong
name_dict = {} 
name_dict
#Truy xuat
#Truy xuat bang key

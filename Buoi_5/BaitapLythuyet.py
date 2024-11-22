# import random

# # Khởi tạo biến c_ với giá trị 100
# c_ = 100

# # Tạo một tuple chứa các số nguyên ngẫu nhiên từ 0 đến 100, với 100 phần tử
# my_tuple = tuple(random.randint(0, c_) for _ in range(c_))
# print("Tuple my_tuple:", my_tuple)

# # Đếm số lượng phần tử chẵn trong tuple bằng cách 1
# dem = 0
# for i in range(len(my_tuple)):
#     if my_tuple[i] % 2 == 0:
#         dem += 1
# print("Số phần tử chẵn trong my_tuple (Cách 1):", dem)

# # Đếm số lượng phần tử chẵn trong tuple bằng cách 2
# even_tuple = tuple(i for i in my_tuple if i % 2 == 0)
# print("Số phần tử chẵn trong my_tuple (Cách 2):", len(even_tuple))

# # Yêu cầu người dùng nhập một số để kiểm tra sự tồn tại trong tuple
# x = int(input("Nhập số x để kiểm tra trong my_tuple: "))

# # Kiểm tra xem x có tồn tại trong tuple hay không
# if my_tuple.count(x) != 0:
#     print(f"my_tuple có chứa số {x}")
# else:
#     print(f"my_tuple không chứa số {x}")

# Tạo một từ điển chứa ID và Họ và tên của sinh viên
students = {
    "2020601001": "Nguyễn Văn A",
    "2020601002": "Trần Thị B",
    "2020601003": "Lê Văn C",
    
}

# In từ điển ra màn hình
print("Danh sách sinh viên:")
print(students)

# Kiểm tra sinh viên có mã "2020601001" có trong từ điển hay không
student_id = "2020601001"
if student_id in students:
    print(f"\nSinh viên có mã '{student_id}' có trong từ điển.")
    print(f"Họ và tên: {students[student_id]}")
else:
    print(f"\nSinh viên có mã '{student_id}' không có trong từ điển.")

# Sao chép các sinh viên có mã là số chẵn sang một từ điển mới
even_id_students = {id: name for id, name in students.items() if int(id) % 2 == 0}

# In từ điển mới chứa sinh viên có mã là số chẵn
print("\nDanh sách sinh viên có mã số chẵn:")
print(even_id_students)

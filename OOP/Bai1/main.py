# class person: name, age
#     intt

# sinhvien(person)
# class sinhvien: msv, diem
#     intt 

# class lophoc: ten_lop, danh sach sinh vien 
#     Them sinh vien 
#     Xoa sinh vien

# name, age :private

from typing import List,  Optional

class Person:
    def __init__(self, name: str, age: int):
        self.__name = name  
        self.__age = age    

    def get_name(self):
        return self.__name

    def set_name(self, name: str):
        if name:
            self.__name = name
        else:
            raise ValueError("Name cannot be empty")

    def get_age(self):
        return self.__age

    def set_age(self, age: int):
        if age > 0:
            self.__age = age
        else:
            raise ValueError("Age must be a positive integer")

    def __str__(self):
        return f"Name: {self.__name}, Age: {self.__age}"

class SinhVien(Person):
    def __init__(self, name: str, age: int, msv: str, diem: float):
        super().__init__(name, age)  # Gọi hàm khởi tạo của lớp cha (Person)
        self.msv = msv 
        self.diem = diem 

    def get_msv(self):
        return self.msv

    def set_msv(self, msv: str):
        if msv:
            self.msv = msv
        else:
            raise ValueError("MSV cannot be empty")

    def get_diem(self):
        return self.diem

    def set_diem(self, diem: float):
        if 0 <= diem <= 10:
            self.diem = diem
        else:
            raise ValueError("Diem must be between 0 and 10")

    def __str__(self):
        return f"{super().__str__()}, MSV: {self.msv}, Diem: {self.diem}"

class LopHoc:
    """
    Lớp đại diện cho một lớp học, chứa danh sách sinh viên.

    Attributes:
        ten_lop (str): Tên của lớp học.
        danh_sach_sinh_vien (list[SinhVien]): Danh sách các sinh viên trong lớp.
    """


    def __init__(self, ten_lop: str, danh_sach_sinh_vien: Optional[List[SinhVien]] = None):
        """
        Khởi tạo lớp học với tên lớp và danh sách sinh viên tùy chọn.

        Args:
            ten_lop (str): Tên của lớp học.
            danh_sach_sinh_vien (list[SinhVien], optional): Danh sách sinh viên ban đầu. Mặc định là None.
        """
        self.ten_lop = ten_lop
        self.danh_sach_sinh_vien = danh_sach_sinh_vien if danh_sach_sinh_vien else []

    def them_sinh_vien(self, sinh_vien: SinhVien):
        """
        Thêm một sinh viên vào danh sách lớp học.

        Args:
            sinh_vien (SinhVien): Sinh viên cần thêm.

        Raises:
            ValueError: Nếu đối tượng không phải là SinhVien.
        """
        if isinstance(sinh_vien, SinhVien):
            self.danh_sach_sinh_vien.append(sinh_vien)
        else:
            raise ValueError("Only objects of type SinhVien can be added")

    def xoa_sinh_vien(self, msv: str):
        """
        Xóa sinh viên khỏi danh sách dựa trên mã số sinh viên.

        Args:
            msv (str): Mã số sinh viên cần xóa.
        """
        self.danh_sach_sinh_vien = [sv for sv in self.danh_sach_sinh_vien if sv.get_msv() != msv]

    def __str__(self):
        """
        Trả về chuỗi biểu diễn danh sách sinh viên trong lớp.

        Returns:
            str: Chuỗi chứa thông tin lớp học và danh sách sinh viên.
        """
        result = f"Lop: {self.ten_lop}\n"
        for sv in self.danh_sach_sinh_vien:
            result += str(sv) + "\n"
        return result

# Sử dụng các lớp
# Tạo đối tượng của lớp Person
person = Person("Nguyen Van A", 30)
print(person)

# Thay đổi giá trị của thuộc tính thông qua setter
person.set_name("Tran Van B")
person.set_age(35)
print(person)

print("=====================================")
# Tạo đối tượng của lớp SinhVien
sinhvien1 = SinhVien("Le Thi C", 20, "SV123", 8.5)
sinhvien2 = SinhVien("Pham Van E", 22, "SV124", 7.5)
sinhvien3 = SinhVien("Nguyen Thi A", 22, "SV126", 7.5)
sinhvien4 = SinhVien("Pham Quynh B", 22, "SV127", 7.5)

lop_hoc = LopHoc("12A1", [sinhvien1, sinhvien2, sinhvien3, sinhvien4])

# Hiển thị danh sách sinh viên trong lớp
print(lop_hoc)

# Xóa sinh viên khỏi lớp
lop_hoc.xoa_sinh_vien("SV123")
print("Sau khi xoa sinh vien:")
print(lop_hoc)
    

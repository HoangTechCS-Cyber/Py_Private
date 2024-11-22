a = set(input("nhap danh sach nguoi dang ky: ").split())
b = set(input("nhap danh sach nguoi da checkin: ").split())
print("danh sach nguoi chua checkin la: ", a - b)
print("Tong so ban da dang ky la: ", len(a),"\n","Tong so ban da check-in la: ",len(b))
#sap xep
sorted_a = sorted(a)
print("Danh sách đã đăng ký (sắp xếp):", sorted_a)

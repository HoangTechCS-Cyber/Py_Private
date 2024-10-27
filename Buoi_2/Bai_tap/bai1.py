# Nhập số nguyên a và b
a = int(input("a = "))
b = int(input("b = "))

# In các phép tính cơ bản
print("a - b = ", a - b)
print("a + b = ", a + b)
print("a * b = ", a * b)
print("a // b = ", a // b)
print("a ** b = ", a ** b)
print("a % b = ", a % b)

# So sánh a và b
if a > b:
    print("a lớn hơn b")
elif a < b:
    print("a nhỏ hơn b")
else:
    print("a bằng b")

# Phép toán logic: and, or, xor
print("a and b:", a and b)
print("a or b:", a or b)
print("a xor b:", a ^ b)

# Kiểm tra nếu a khác b
if not a == b:
    print("a và b khác nhau")
else:
    print("a và b bằng nhau")

# Phép dịch bit
print("a << 5:", a << 5)
print("a >> 6:", a >> 6)

# Đảo bit của a. EM khong bit lam
# a_ = not bin(a)
# print("Đảo ngược bit của a là:", a_)

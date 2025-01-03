import numpy as np 

# mang 1 chieu 
arr = np.array([1, 2, 3 , 4, 5])

#mang hai chieu
arr2 = np.array([[1, 2, 3], [1, 2, 3], [1, 2, 3]])

print(arr)
print(arr2)
#tao mang toan 0
arr0 = np.zeros(5) #tao 5 con 0
#tao mang toan 1
arr1 = np.ones(5) #tao 5 con 1
#tao mang tu 0 den 9
arange = np.arange(10) # 0 1 2  3 4 5 6 7 8 9


#cong tru mang
a = np.array([1, 2, 3, 4, 5])
b = np.array([5, 4, 3, 2, 1])

#cong tru, nhan, chia
print("a + b:", a + b)  
print("a - b:", a - b)
print("a * b:", a * b)
print("a / b:", a / b)

#tao mang tu mot day so 
#10 so tu 0 den 100
linspace = np.linspace(0, 100, 10)

# nhan ma tran
A = np.array([[1, 2, 3], [4, 5, 6]])
B = np.array([[7, 8], [9, 10], [11, 12]])

C = np.dot(A, B)
print("C =",C)
#tinh tong cac gia tri trong mang 
TongAB = np.sum(A) + np.sum(B)
print("Tong cac phan tu A và B:",TongAB)
print("Trung binh cong cua A", np.mean(A))
print("Độ lệch chuẩn cua A:", np.std(A))
print("Tính nghịch đảo ma trận:", np.linalg.inv(A))
a = tuple(map(int, input("A = ").split()))
b = tuple(input("B = ").split())
tbc = sum(a) / len(a)
dem = sum(1 for i in a if i > tbc)  
print("tbc", tbc)
print("So luong phan tu lon hon tbc trong a: ", dem)
# chia tuple thanh hai tuple chan le 
odd = ()
even = ()
odd = tuple(i for i in a  if i % 2==0)
even = tuple(i for i in a if i %2 !=0)
print("odd: ", odd, "\n", "even: ", even)   
#dem so lan ki tu k xuat hien
k = input("k = ")
print("So lan xuat hien cua k trong B", b.count(k))
string_ = tuple(s for s in b if len(s) >= 5)
print("cac phan tu trong tuple B co do dai lon hon bang 5: ",string_)
c = tuple(zip(a, b))
print(c)



print("Chao mung den CLB Tin Hoc HIT")
print("CLB Tin Hoc HIT truc thuoc Khoa CNTT  - “10 diem”")
st = "CLB Tin Hoc HIT truc thuoc Khoa CNTT"
for i in st:
    if( i >= 'A' and i <= 'Z'):
        print(i)
for i in st:
    if( i >= 'a' and i <= 'z'):
        print(i)
if st.find("CNTT") == -1:
    print("NO")
else: print("YES")
for i in st:
    if( i >= 'A' and i <= 'Z'):
        i.lower()
    if( i >='a' and i <= 'z'): 
        i.upper()
print(st)
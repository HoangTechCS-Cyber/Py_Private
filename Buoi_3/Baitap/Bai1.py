x = float(input( "x = "))
n = int(input( "n = "))
def giaithua(a) :
    if a== 0 or a == 1 :
        return 1
    else:
        return a * giaithua(a-1) 
ans = 1 + x
for i in range(2, n) :
    
    ans += (x**i) / giaithua(i)

print("1: ",ans)
ans_ =1
for i in range(2, n, 1):
    ans+= 1 / giaithua(i)
print("2: ", ans_)


    
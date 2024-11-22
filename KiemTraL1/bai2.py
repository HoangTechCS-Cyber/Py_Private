def count_(word):
    cnt = {}
    for i in word:
        cnt[i] = cnt.get(i, 0) + 1  
    return cnt

s = input("Nhập s: ")
rep = count_(s)
rep = dict(sorted(rep.items())) 
print(rep)

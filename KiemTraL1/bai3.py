def code_(s):
    stack = [] 
    tmp = "" 
    curr_str = ""  
    for i in s:
        if i.isdigit():  
            tmp += i
        elif i == '[': 
            dem = int(tmp) if tmp else 0  
            stack.append((curr_str, dem))
            curr_str = "" 
            tmp = "" 
        elif i == ']':  
            prev, repeat = stack.pop()
            curr_str = prev + curr_str * repeat  
        else:  
            curr_str += i

    return curr_str

s = input("Nhập code: ")
print("Chuỗi giải mã:", code_(s))

# def check(year):
#     if year % 4 == 0:
#         if year % 100 == 0:
#             if year % 400 == 0:
#                 return True
#             else:
#                 return False
#         else:
#             return True
#     else:
#         return False
    
# check1 = lambda year: year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)



# print(check(21), check1(21))


'''
Viet ham nhan va mot chuoi danh sach cac chuoi va tra ve mot tuple chua tu ngan nhat va tu dai nhat
trong danh sach, theo thu tu do. Neu co nhieu tu co do dai ngan nhat dai nhat giong nhau,
tra ve vi tri tu ngan nhat hoac dai nhat dau tien duoc tim thay
'''
# def solve(*args):
#     min_ = (args[0], 0) 
#     max_ = (args[0], 0) 
#     for i in range(len(args)):
#         if len(args[i]) < len(min_[0]):
#             min_ = (args[i], i)
#         if len(args[i]) > len(max_[0]):
#             max_ = (args[i], i)
#     return min_, max_
# result = solve('ngan', 'dai', 'dainhat', 'dai', 'daidahahahidaidadiadi')
# print("Min:", result[0]) 
# print("Max:", result[1])

def short_long_str(strings:list[str]) -> dict:
    shortest = min(strings, key = len)
    longtest = max(strings, key = len)
    
    short_word_index = [index for index, value in enumerate(strings) if value == shortest]
    long_word_index = [index for index, value in enumerate(strings) if value == longtest]
    return {
        'ngannhat' : short_word_index[0],
        'dainhat' : long_word_index[0],
    }
inp = ["'ngan'", "'dai'", "'dainhat'"," 'dai'", "'daidahahahidaidadiadi'"]

mydict =  short_long_str(inp)
print(mydict)
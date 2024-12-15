# # def hello(name, age):
# #     print(f"Hello world {name}")
# #     print(f"age={age}")
# #     return name, age

# # name, age = hello(age = 25, name = "HIT")
# # print(f"Nam of the function is {name}")
# # print(f"Age of the function is {age}")

# # #tinh tong 
# # def tong(a, b, c):
# #     return a + b + c
# # # args 
# # def tinh_tong(*args):
# #     tong_ = 0
# #     for i in args:
# #         tong_ += i
# #     return tong_
# #     # return sum(args)
# # tong = tinh_tong(1,2,3,5,6,7)
# # print(tong)

# # def calc_mod( a, b, mod = 1e9,*agrs,**kwarg):
# #     if kwarg['type'] == 'add':
# #         return (a + b) % mod
# #     elif kwarg['type'] == 'sub':
# #         return (a - b + mod) % mod
# #     elif kwarg['type'] == 'mul':
# #         return a * b % mod
# # print(calc_mod(1, 2, type = 'add'))
# # print(calc_mod(10,2, type = 'sub'))

# def gthua(n):
#     if n == 1: 
#         return 1
#     return n * gthua(n - 1)
# print(gthua(5))  


# # def gthua2(n:int) -> tuple[int, int]:
#     if n == 1:
#         return 1, 1
#     return n, n*gthua2(n-1)
# print(gthua2(5))



#lambda : ham an danh

ave = lambda a ,b, c: (a + b + c) // 3
print(ave(3, 5, 7)) #5

'''
tuong duong voi 
def ave(a, b, c):
    return (a + b + c) / 3
'''
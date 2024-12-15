import random

def Tao(N):
    cn = ["CNTT", "KHMT", "KTPM", "HTTT", "DAPT"]
    acc = {}
    
    for i in range(N):
        id = 2023600000 + i
        password = random.choice(cn) + str(id)
        acc_name = f"Account{i + 1}"
        acc[acc_name] = {
            "Username": id,
            "Password": password
        } 
    return acc

N = int(input())
account_info = Tao(N)
for account, info in account_info.items():
    print(f"{account}: {info}")
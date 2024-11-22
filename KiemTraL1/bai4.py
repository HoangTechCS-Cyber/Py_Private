#hetcuu


def xly(data):
    dict = {}

    for entry in data:
        pairs = entry.split(";")
        for pair in pairs:
            key, val = pair.split("=")
            key, val = key.strip(), val.strip()

            if val.isdigit():
                val = int(val)
            elif val.replace('.', '', 1).isdigit() and val.count('.') == 1:
                val = float(val)

            if key not in dict:
                dict[key] = []
            dict[key].append(val)
    
    result = {}
    
    return dict, result

data = input("Nhập data: ").split("; ")

dict, result = xly(data)
print("main: ", dict)
print("out: ", result)

def xly(data):
    from collections import defaultdict 
    dict = defaultdict(list)

    for entry in data:
        pairs = entry.split(";")
        for pair in pairs:
            key, val = pair.split("=")
            key, val = key.strip(), val.strip()
            
            if val.isdigit():
                val = int(val)
            else:
                try:
                    val = float(val)
                except ValueError:
                    pass
            dict[key].append(val)
    
  
    result = {}
    for key, vals in dict.items():
        unique_vals = set(vals)
        result[key] = {
            "unique_count": len(unique_vals),
            "max_val": max(vals) if all(isinstance(v, (int, float)) for v in vals) else None,
            "max_length": max(len(str(v)) for v in unique_vals) if any(isinstance(v, str) for v in vals) else None
        }
    
    return dict(dict), result

data = input("Nhập data: ").split("; ")

dict, result = xly(data)
print("Dictionary chính:", dict)
print("Kết quả phân tích:", result)

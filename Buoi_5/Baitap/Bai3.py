def swap(d):
    if len(d) != len(set(d.values())):
        return None
    sw = {v: k for k, v in d.items()}
    return sw

dict = {'a': 1, 'b': 2, 'c': 3}
print(swap(dict))
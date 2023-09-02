def list_xor(n, list1, list2):
    if n in list1 and n in list2:
        return False
    elif n not in list1 and n not in list2:
        return False
    else:
        return True
    
print(list_xor(1, [0, 2, 3], [0, 5, 6]))

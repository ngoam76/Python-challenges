
count = []

def consecutive_zeros(binary_string):
    list_0 = []
    for i in binary_string:
        if i == "0":
            list_0.append(binary_string.index(i))
        elif i == "1":
            count.append(len(list_0))
            list_0 = []
    
    max_zeros = max(count)
    return max_zeros


print(consecutive_zeros("100111111000001000000000110"))
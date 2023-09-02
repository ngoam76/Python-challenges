def zap(list_1, list_2):
    list_result = []
    for i in range(len(list_1)):
            tuple_result = (list_1[i], list_2[i])
            list_result.append(tuple_result)
    return list_result

print(zap([0, 1, 2, 3], [5, 6, 7, 8]))
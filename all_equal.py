def all_equal(given_list):
    for i in range(len(given_list) - 1):
        if given_list[i] != given_list[i + 1]:
            return False
    return True

print(all_equal([1, 1, 1, 1, 1]))
    
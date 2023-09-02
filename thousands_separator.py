def format_number(number):
    result_str = ""
    number_str_reversed = "".join(reversed(str(number)))
    for i in range(len(number_str_reversed)):
        result_str += number_str_reversed[i]
        if i % 3 == 2 and i != len(number_str_reversed)-1:
            result_str += ","
    result_str = "".join(reversed(result_str))
    return result_str

print(format_number(1000000))
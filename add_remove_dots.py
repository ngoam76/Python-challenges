def add_dots(old_string):
    empty_string = ""
    l = []
    for i in old_string:
        empty_string = i + "."
        l.append(empty_string)
        new_string = "".join(l)
    print(new_string)
    return new_string

def remove_dots(old_string):
    new_string = old_string.replace(".","")
    print(new_string)


add_dots("Test")
remove_dots("T.e.s.t.")

remove_dots(add_dots("Test"))

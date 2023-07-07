def double_letters(word):
    list_letter = []
    for n in word:
        list_letter.append(n)
    for i,j in list_letter:
        if list_letter.index(i) < list_letter.index(j) and i == j :
            print("False")
        else:
            print("True")


double_letters("Hello")
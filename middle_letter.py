word = input("Insert the word: ")
def middle_letter(word):
    last_index = len(word) - 1
    for i in word:
        if word.index(i) == last_index/2:
            print(i)
        else:
            print("")

middle_letter(word)
def is_anagram(word1, word2):
    list_word1 = list(word1)
    list_word1.sort()
    list_word2 = list(word2)
    list_word2.sort()
    if list_word1 == list_word2:
        print("True")
        return True
    else:
        print("False")
    return False


is_anagram("typhoon", "opython")
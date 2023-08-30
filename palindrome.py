def palindrome(word):
    for i in range(len(word)):
        if word[i] == word[len(word)-i-1]:
            print("TRUE")
        else:
            print("FALSE")


palindrome("abcba")
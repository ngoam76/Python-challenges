def double_letters(word):
    for i in range(len(word)-1):
      if word[i] == word[i+1]:
         print("True")
         return True
    return False


double_letters("Nono")
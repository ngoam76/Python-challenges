def count(word):
    l = []
    for i in word:
        if i == "-":
            l.append(word.index(i))
            x = len(l)
    count = x + 1
    print(count)
    return count


count("He-llo-my-name-is-chau")

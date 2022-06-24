def count_words():
    words_counted = {}
    with open("./file/articles.txt") as fp:
        for line in fp:
            line = line[:-1]
            words = line.split()
            for word in words:
                if word not in words_counted:
                    words_counted[word] = 0
                words_counted[word] += 1
    # res = words_counted
    res = sorted(words_counted.items(), key=lambda x: x[1], reverse=True)
    return res


res = count_words()
print(res)
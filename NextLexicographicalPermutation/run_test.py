from NextLexicographicalPermutation import findNextLex


def runNextLex(word=None):
    if word is None:
        word = input()
    return lex.findNextLexicographical(word)


#######################
lex = findNextLex.nextLexPermutation()
words = ["lmno", "dcba", "dcbb", "abdc", "abcd", "fedcbabcd"]
for word in words:
    print(runNextLex(word))

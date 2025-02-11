def permutations(s, prefix=""):
    if len(s) == 0:
        print(prefix)
    else:
        for i in range(len(s)):
            permutations(s[:i] + s[i+1:], prefix + s[i])

def combinations(s, start=0, prefix=""):
    if prefix:
        print(prefix)
    for i in range(start, len(s)):
        combinations(s, i + 1, prefix + s[i])

word = "аав"

print("Перестановки:")
permutations(word)


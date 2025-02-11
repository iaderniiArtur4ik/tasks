import itertools2

word = "аав"

permutations = set(itertools.permutations(word))

permuted_words = [''.join(p) for p in permutations]

for perm in sorted(permuted_words):
    print(perm)

print(f"Количество уникальных перестановок: {len(permuted_words)}")
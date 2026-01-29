def count_a(s):
    return s, s.count('a')

inputs = ["aaab", "aba", "aaaa", "bbbb"]

for i in inputs:
    print(count_a(i))

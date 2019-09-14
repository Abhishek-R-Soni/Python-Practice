# sort array by using Counter

from collections import Counter

str = "02101"

x = Counter(str)

print("0" * x['0'], end="")
print("1" * x['1'], end="")
print("2" * x['2'])
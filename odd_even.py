#           Odd Even

num = range(1,11)

odd = [odd for odd in num if odd%2 != 0]
print(odd)

even = [even for even in num if even%2 == 0]
print(even)

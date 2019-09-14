def sum(num):
    total = 0

    for n in range(num):
        total += square(n)
    return total

def square(num):
    return num**num


s = sum(4)
print(s)

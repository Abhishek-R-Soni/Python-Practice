def sum(num,*values):
    total = 0
    for i in values:
        total += i
    return total 

print(sum(1))
print(sum(1,2))
print(sum(1,2,3))

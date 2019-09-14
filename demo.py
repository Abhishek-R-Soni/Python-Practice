

nos = [1,5,3,5,7,9]
min = 999

length = len(nos)-1
i = 1
while(length > 0):
    if min > nos[i] - nos[i-1]:
        min = nos[i] - nos[i-1]
    length -= 1
    i = i+1

print(abs(min))
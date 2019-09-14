#   Find first and last occurrence of x
'''
Example:
Input:
2
9
1 3 5 5 5 5 67 123 125
5
9
1 3 5 5 5 5 7 123 5 125
7

Output:
2 5
6 6
'''
nos = [1,3,5,5,5,5,67,123,125]
print(nos)

if 5 in nos:
    print(nos.index(5)+1)
else:
    print("n")

cnt = 0
for i in reversed(nos):
    cnt += 1
    if 5 == i:
        print(cnt)
        break
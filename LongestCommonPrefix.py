
array = input().split()
l = 999
com = []
# for find Smallest string
for i in array:
    if l > len(i):
        l = len(i)

# for find longest common sequence
for i in range(l):    
    char = array[0][i]

    for j in range(1,len(array)):
        if(char != array[j][i]):
            break
        if j == len(array)-1:
            com.append(array[0][i])
print(com)
    
'''
Example:
Input:
2
4
geeksforgeeks geeks geek geezer
3
apple ape april

Output:
gee
ap
'''
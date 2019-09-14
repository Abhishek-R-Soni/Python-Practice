#   Reversing the vowels

'''
Example:
Input:
4
geeksforgeeks
practice
wannacry
ransomware

Output:
geeksforgeeks
prectica
wannacry
rensamwora
'''

string = ["rensamwora"]
init = 0
last = len(string)
i1 = ""
i2 = ""
mid = last//2

def start(x):
    for i in range(x,len(string)//2):
        if(string[i] == "a" or string[i] == "e" or string[i] == "i" or string[i] == "o" or string[i] == "u"):
            return string.index(i)

def end(y):
    while(mid <= y):
        if(string[y] == "a" or string[y] == "e" or string[y] == "i" or string[y] == "o" or string[y] == "u"):
            return string.index(y)
        y -= 1

while(init != -1 or last != -1):
    i1 = start(init)    
    i2 = end(last-1)

    print(i1, " ",i2)
    break
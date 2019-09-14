arr = [64,25,122,22,11]
index = 0
id = 0

def getMinIndex(init):
    min = 999
    for i in range(init,len(arr)):
        if(min > arr[i]):
            min = arr[i]
            index = i
    return index

for i in range(len(arr)):
    id = getMinIndex(i)
    arr[i], arr[id] = arr[id], arr[i]

print(arr)
# Binary Search

array = [1,2,3,4,5,7,8,6]

array.sort()
search = 5
# search = -384848

low = 0
high = len(array)-1

mid = (high + low)//2

while(low < high):    
    
    if(search == array[mid]):
        print("Found : ", array[mid])
        break

    if(search > array[mid]):
        low = mid 
        high = len(array)-1
        mid = (high + low)//2
    else:
        high = mid
        mid = (high + low)//2

    if((low + 1) == high or (high - 1) == low):
        print("Not found Yet, try another number...!")
        break 

'''
    Simple way

    if search in array:
        print(array.index(search)+1)
    else:
        print("Not found Yet, try another number...!")

'''

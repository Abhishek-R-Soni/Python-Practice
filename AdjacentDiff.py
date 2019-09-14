# 7 98 56 43 45 23 12 8
import math
array = [7,98,56,43,45,23,12,8]

for i in array:
    if(i < 54):
        if(abs(i//10 - i%10) == 1):
            print(i)

# permutation

def fect(f):
    ans = 1
    for n in range(1,f+1):
        ans = ans * n
    return ans

# enter message
msg = (list)(input("Enter msg : "))
# find possible values
l = len(msg)
f = fect(l)

# print 
for i in range(0,l):
    print(f"{msg[i]} {msg[(i+1)%l]} {msg[(i+2)%l]}")
    print(f"{msg[i]} {msg[(i+2)%l]} {msg[(i+1)%l]}")


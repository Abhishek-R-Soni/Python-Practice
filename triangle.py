# print * triangle

n = 10
cnt = -1
for i in range(1,n+1):
    cnt += 2
    print(' '*(n-i), '*'*cnt, ' '*(n-i))


# output 
#           *
#          ***
#         *****
#        *******
#       *********
#      ***********
#     *************
#    ***************
#   *****************
#  *******************

# convert list to str
names = ['Abhi', 'Dhimant', 'Khushi']
# print(' '.join(names))  # output : Abhi Dhimant Khushi
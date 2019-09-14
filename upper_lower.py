#               camel & snake case

names = ["abhishek","khushi","dhimant"]

c = 0
#for name in names:
while c < len(names[0]):
       if c%2 == 0:
           names[c].upper()
           c = c+1
       else:
           names[c].lower()
           c = c+1
       print(names)
        

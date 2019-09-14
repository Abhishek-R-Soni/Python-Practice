# Password generator
names = input()
names = names.split(",")
length = 0
final_str = ""
temp = []
max = 0

for name in names:
    temp = name.split(":")        
    length = len(temp[0])-2
    
    for i in (temp[1]):
        i = int(i)
        if i <= length:
            if max < i:
                max = i
    if max == 0:
        final_str += "X"
        pass      
    final_str += temp[0][max]
    max = 0

print("\nPassword : " + final_str)
# input : "Abhishek":34848,"Mayur":4739,"Friends":2949,"Yeah":9889
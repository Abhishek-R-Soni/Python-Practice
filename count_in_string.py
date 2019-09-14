#               Count uppercase,lowercase,space etc

str = input("Enter Your Message : ")

upr,lwr,spc,num,prt,etc = 0,0,0,0,0,0

for char in str:
    if char.isupper():
        upr += 1
    elif char.islower():
        lwr += 1
    elif char.isspace():
        spc += 1
    elif char.isnumeric():
        num += 1
    elif char.isprintable():
        prt += 1
    else:
        etc += 1
        
print(f"Upper : {upr}\nLower : {lwr}\nSpace : {spc}\nNum : {num}\nprint : {prt}\nEtc : {etc}")

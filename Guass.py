#   guass jordan method

# Getting values from user
equa1 = list(input("Enter Data : "))
equa2 = list(input("Enter Data : ")) 

# dispaly co-efficiency matrix
print("co-efficiency matrix")
i=0
while i<3:
    equa1[i] = int(equa1[i])
    equa2[i] = int(equa2[i])
    i += 1
print(equa1)
print(equa2)

# logic of diagonal matrix
print("\nDiagonal Matrix")
temp = (-1) * equa2[0]

temp_matrix = equa1
temp_matrix = [i*temp for i in temp_matrix]
 
i=0
while i<3:
    equa2[i] = temp_matrix[i] + equa2[i]
    i += 1
print("\n   (1)")
print(equa1)
print(equa2)

print("\n   (2)")
equa2 = [i*(-1) for i in equa2]
print(equa1)
print(equa2)

print("\n   (3)")
temp_matrix = [i*(-1) for i in equa2]
i=0
while i<3:
    equa1[i] = equa1[i] + temp_matrix[i]
    i += 1
print(equa1)
print(equa2)

# solution

print(f"\nSolution :{equa1[2]},{equa2[2]}")

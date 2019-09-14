student = ["bablu","abhi"]

midterm = [67,34]

final = [89,78]

print({data[0]:max(data[1],data[2]) for data in zip(student,midterm,final)})

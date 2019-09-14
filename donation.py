#       donation

donation_list = dict(Abhishek=500,Khushi=1000,Dhimant=600)

donation = 0

# sum of donation
for don in donation_list.values():
    donation += don
print(f"total donation :{donation}")

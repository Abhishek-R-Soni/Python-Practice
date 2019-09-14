#       concatenation solution

# add first & last name with space

name = {"First":"#Abhishek",
        "Last":"Soni"
        }
full_name = name["First"] + " R " + name["Last"]
print(full_name)


# format()

temp_name = " {} ".format(name["First"],name["Last"])
print(temp_name)

full_name = f"{name['First']} {name['Last']}"
print(full_name)

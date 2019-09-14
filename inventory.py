#       copy dict to other dict

inventory = {"croissant":19,
             "bagel":4,
             "muffin":8,
             "cake":1
            }
#for k,v in inventory.items():
#    print(f"Key is : {k}\nValues is : {v}")

stock_list = inventory.copy()
print("After copy")
for k,v in stock_list.items():
    print(f"Key is : {k}\nValues is : {v}")

# update cake value
stock_list["cake"] = 29
print("After change cake")
print(stock_list["cake"])

# delete item

stock_list.pop("cake")
print("After delete cake")
print(stock_list)

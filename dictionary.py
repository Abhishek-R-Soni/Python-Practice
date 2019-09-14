#               dictionary

shopping_items = {"Name":"#Abhishek R Soni",
                  "Product":"Mobile",
                  "Price":"10999/-",
                  "Model":"Mi Y2",
                  "status":"booked"
                 }
#print(shopping_items)
#print(shopping_items["Model"])#Accessing perticuler item

#Accessing keys
#for k in shopping_items.keys():
#    print(k)

#Accessing values
#for v in shopping_items.values():
#    print(v)

#Accessing both items
#for itm in shopping_items.items():
#    print(itm)
    
#Accessing both items
#for k,v in shopping_items.items():
#    print(f"key is {k} : value is {v}")

# usage of in 
#print("Name" in shopping_items)
#print("Name" in shopping_items.keys())
#print("Name" in shopping_items.values())
#print("Name" in shopping_items)

# deleting items
#print(shopping_items.pop("Name"))
#for k,v in shopping_items.items():
# print(f"key is {k} : value is {v}")    

# deleting values
#print(shopping_items.popitem())
#for k,v in shopping_items.items():
# print(f"key is {k} : value is {v}")  

# update new shopping_items 
temp = {"Brand":"Xiomi"}
shopping_items.update(temp)
for k,v in shopping_items.items():
 print(f"key is {k} : value is {v}")

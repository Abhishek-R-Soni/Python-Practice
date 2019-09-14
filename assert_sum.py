def sum(no1,no2):
    assert no1>0 and no2>0 ,"Contain negative value"
    print(no1+no2)

def junk_food(food):
    assert food not in ["Ice-cream","Candy","Butter"], "not junk food, Good!"
    print(food)

junk_food("Bu")
sum(10,20)

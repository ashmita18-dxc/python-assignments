class products1:
    def __init__(p,i,n,c,d,r,b,ca):
        p.id=i
        p.name=n
        p.cost=c
        p.discount=d
        p.rating=r
        p.brand=b
        p.category=ca
    def show(li):
        print("ID---NAME---COST---DISC---RATING---BRAND---CATEGORY")
        data="{id}   {name}   {cost}   {discount}   {rating}   {brand}   {category}"
        for i in li:
            print(data.format(**i.__dict__))

p1=products1("1","Note Pro",16000,10,4,"Xiomi","Mobile")
p2=products1("2","M10",19000,20,4,"Samsung","Mobile")
p3=products1("3","OnePlus7",34000,10,4.9,"OnePlus","Mobile")
p4=products1("4","Note 8Pro",18500,25,4,"Xiomi","Mobile")
p5=products1("5","Galaxy A7",10000,5,3,"Samsung","Mobile")
p6=products1("6","Iphone X",45000,15,3.6,"IPhone","Mobile")

plist=[p1,p2,p3,p4,p5,p6]
products1.show(plist)

print("1.Sort by Cost-->Low to High")
print("2.Sort by Cost-->High to Low")
print("3.Sort by Rating")
print("4.Sort by Discount-->Low to High")
print("5.Sort by Discount-->Low to Low")
option={
    "1":["cost",False],
    "2":["cost",True],
    "3":["rating",True],
    "4":["discount",False],
    "5":["discount",True]
}
choice=input("Enter choice: ")

mysort = lambda element: element[option[choice][0]]
products1.sort(key=mysort)
products1.show(plist)



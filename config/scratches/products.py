Products=[
{
        "pid":"1",
        "name":"Asus1",
        "cost":50000,
        "brand":"Asus",
        "rating":4,
        "discount":10,
        "category":"Laptop"
    },
       {
        "pid":"2",
        "name":"Hp1",
        "cost":69000,
        "brand":"Hp",
        "rating":4.5,
        "discount":12,
        "category":"Laptop"
    },
       {
        "pid":"3",
        "name":"Lenovo1",
        "cost":42000,
        "brand":"Lenovo",
        "rating":4.2,
        "discount":14,
        "category":"Laptop"
    },
       {
        "pid":"4",
        "name":"Asus2",
        "cost":650000,
        "brand":"Asus",
        "rating":4.4,
        "discount":11,
        "category":"Laptop"
    },
       {
        "pid":"5",
        "name":"Hp2",
        "cost":55000,
        "brand":"Hp",
        "rating":4.5,
        "discount":17,
        "category":"Laptop"
    },
       {
        "pid":"6",
        "name":"Lenovo2",
        "cost":100000,
        "brand":"Lenovo",
        "rating":4.7,
        "discount":7,
        "category":"Laptop"
    }
]
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
Products.sort(key=mysort,reverse=option[choice][1])
print(Products)

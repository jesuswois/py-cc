# 6-12. Extensions: We’re now working with examples that are complex enough
# that they can be extended in any number of ways. Use one of the example pro-
# grams from this chapter, and extend it by adding new keys and values, chang-
# ing the context of the program or improving the formatting of the output.

person = {
    "first_name":"john",
    "last_name":"doe",
    "age":30,
    "city":"dummy land",
    "visited_places":[
        {
            "country":"mexico",
            "city":"puebla",
            "date":"15/02/1996"
        },
        {
            "country":"united states",
            "city":"chicago",
            "date":"23/06/2005"
        },
        {
            "country":"russia",
            "city":"moscow",
            "date":"06/01/2010"
        }
    ]
}

print("First Name: "+person["first_name"].title())
print("Last Name: "+person["last_name"].title())
print("Age: "+str(person["age"]))
print("City: "+person["city"].title())
print((person["first_name"]+" "+person["last_name"]).title()+"'s visited places are:")
for visited_place in person["visited_places"]:
    print("\t"+visited_place["city"].title()+", "+visited_place["country"].title()+" in "+visited_place["date"])


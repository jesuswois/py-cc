# 6-11. Cities: Make a dictionary called cities. Use the names of three cities as
# keys in your dictionary. Create a dictionary of information about each city and
# include the country that the city is in, its approximate population, and one fact
# about that city. 
# The keys for each city’s dictionary should be something like
# country, population, and fact. Print the name of each city and all of the infor-
# mation you have stored about it.

cities = {
    "puebla":{
        "country":"méxico",
        "population":6580000,
        "fact":"Fourth biggest city in México"

    },
    "chicago":{
        "country":"united states",
        "population":2722000,
        "fact":"Known as the city that never sleeps"
    },
    "moscow":{
        "country":"russia",
        "population":12000000,
        "fact":"The city has history that dates back to 1147"
    }
}

for city, city_info in cities.items():
    print("\n"+city.title()+"'s information is:")
    print("\tCountry: "+city_info["country"].title())
    print("\tPopulation: "+str(city_info["population"]))
    print("\tFact: "+city_info["fact"])
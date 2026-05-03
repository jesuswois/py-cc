# 6-2. Favorite Numbers: Use a dictionary to store people’s favorite numbers.
# Think of five names, and use them as keys in your dictionary. Think of a favorite
# number for each person, and store each as a value in your dictionary. Print
# each person’s name and their favorite number. For even more fun, poll a few
# friends and get some actual data for your program.

favorite_numbers = {
    "evan":4,
    "dennis":1,
    "dummy":5,
    "phillip":10,
    "joe":0
}

print("The favorite number of each person is:")
print("\t-Evan: "+str(favorite_numbers["evan"]))
print("\t-Dennis: "+str(favorite_numbers["dennis"]))
print("\t-Dummy: "+str(favorite_numbers["dummy"]))
print("\t-Phillip: "+str(favorite_numbers["phillip"]))
print("\t-Joe: "+str(favorite_numbers["joe"]))

# 6-10. Favorite Numbers: Modify your program from Exercise 6-2 (page 102) so
# each person can have more than one favorite number. Then print each person’s
# name along with their favorite numbers.

print("")

favorite_numbers = {
    "evan":[5,1],
    "dennis":[1,9,3],
    "dummy":[4,2,6,9],
    "phillip":[10,5,8],
    "joe":[0,8]
}

for name, numbers in favorite_numbers.items():
    print(name.title()+": "+str(numbers))
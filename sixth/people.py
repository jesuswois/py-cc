# 6-7. People: Start with the program you wrote for Exercise 6-1 (page 102).
# Make two new dictionaries representing different people, and store all three
# dictionaries in a list called people. Loop through your list of people. As you
# loop through the list, print everything you know about each person.
person_1 = {
    "first_name":"robert",
    "last_name":"doe",
    "age":27,
    "city":"georgia"
}
person_2 = {
    "first_name":"john",
    "last_name":"doe",
    "age":40,
    "city":"dummy land"
}
person_3 = {
    "first_name":"jane",
    "last_name":"doe",
    "age":32,
    "city":"dummy land"
}

people = [person_1, person_2, person_3]

for person in people:
    print(person)
# 6-8. Pets: Make several dictionaries, where the name of each dictionary is the
# name of a pet. In each dictionary, include the kind of animal and the owner’s
# name. Store these dictionaries in a list called pets. Next, loop through your list
# and as you do print everything you know about each pet.
crail = {
    'kind':'cuyo',
    'owner':'vanessa'
}
tafi = {
    'kind':'dog',
    'owner':'jia'
}
terror = {
    'kind':'dog',
    'owner':'william'
}
pets = [crail, tafi, terror]

for pet in pets:
    print(pet["owner"].title()+" has a "+pet["kind"]+"!")
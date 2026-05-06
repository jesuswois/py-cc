# 8-10. Great Magicians: Start with a copy of your program from Exercise 8-9. Write a function called
# make_great() that modifies the list of magicians by adding the phrase the Great to each magician's name
# Call show_magicians() to see that the list has actually beed modified
magicians = ["euler", "wizard", "brujo", "magic man", "joe"]

def show_magicians(magicians_list):
    print("The list of magicians consists of:")
    for magician in magicians_list:
        print("\t-"+magician.title())

def make_great(magicians_list):
    changed_magicians = []
    while magicians_list:
        current_magician = magicians_list.pop()
        current_magician = "The Great "+current_magician.title()
        changed_magicians.append(current_magician)
    for magician in changed_magicians:
        magicians_list.append(magician)


show_magicians(magicians)
make_great(magicians)
show_magicians(magicians)

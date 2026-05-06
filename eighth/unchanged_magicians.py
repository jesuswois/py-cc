# 8-11. Unchanged Magicians: Start with your work from Exercise 8-10. Call the function make_great()
# with a copy of the list of magicians names. Because the original list will be unchanged, return 
# the new list and store it ina separate list. 

# Call show_magicians with each list to show that you have one list of the original names and one 
# list with The Great added to each magician's name.

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
    return magicians_list

print("\n\t---\tOriginal List\t---\t\n")
show_magicians(magicians)
great_magicians_list = make_great(magicians[:])
print("\n\t---\tGreat Magicians List\t---\t\n")
show_magicians(great_magicians_list)
print("\n\t---\tOriginal List\t---\t\n")
show_magicians(magicians)
print("\n")
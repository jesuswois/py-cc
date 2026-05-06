# 8-9. Magicias: Make a list of magician's names. Pass the list to a function called show_magicians(),
# which prints the name of each magician in the list
magicians = ["euler", "wizard", "brujo", "magic man", "joe"]

def show_magicians(magicians_list):
    print("The list of magicians consists of:")
    for magician in magicians_list:
        print("\t-"+magician.title())

show_magicians(magicians)


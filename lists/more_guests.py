# 3-6. More Guests
# Start with your program from Exercise 3-4 or Exercise 3-5.

# Add a print statement to the end of your program informing people that 
# you found a bigger dinner table.

# Use insert() to add one new guest to the beginning of your list.
# Use insert() to add one new guest to the middle of your list.
# Use append() to add one new guest to the end of your list.

# Print a new set of invitation messages, one for each person in your list.

guests = ["jose","roberto","andrea"]

print("Las siguientes personas estan invitadas a una cena!" \
    "\n\t1.- "+guests[0].title()+
    "\n\t2.- "+guests[1].title()+
    "\n\t3.- "+guests[2].title())

new_guest = "canela"

print("\nEspera... "+guests[1].title()+" no podrá venir. Invitemos mejor"
    "a "+new_guest+".\n")

guests[1] = new_guest

print("Las siguientes personas estan invitadas a una cena!" \
    "\n\t1.- "+guests[0].title()+
    "\n\t2.- "+guests[1].title()+
    "\n\t3.- "+guests[2].title())
# 3-5. Changing Guest List
# Start with your program from Exercise 3-4.

# Add a print statement at the end of your program stating the name of 
# the guest who can’t make it.

# Modify your list, replacing the name of the guest who can’t make it 
# with the name of the new person you are inviting.

# Print a second set of invitation messages, one for each person who is 
# still in your list.

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
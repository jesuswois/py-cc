# 3-9. Dinner Guests: Working with one of the programs from Exercises 3-4
# through 3-7 (page 46), use len() to print a message indicating the number
# of people you are inviting to dinner.

guests = ["jose","roberto","andrea"]

print("Las siguientes personas estan invitadas a una cena!" \
    "\n\t1.- "+guests[0].title()+
    "\n\t2.- "+guests[1].title()+
    "\n\t3.- "+guests[2].title())

print("\nDando un total de "+str(len(guests))+" invitados!")
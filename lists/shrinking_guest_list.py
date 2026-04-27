# 3-7. Shrinking Guest List
# Start with your program from Exercise 3-6.

guests = ["jose","roberto","andrea"]

print("Las siguientes personas estan invitadas a una cena!" \
    "\n\t1.- "+guests[0].title()+
    "\n\t2.- "+guests[1].title()+
    "\n\t3.- "+guests[2].title())

new_guest = "canela"

print("\nEspera... "+guests[1].title()+" no podrá venir. Invitemos mejor"
    "a "+new_guest+".\n")

guests[1] = new_guest

print("Las siguientes personas estan invitadas a la cena!" \
    "\n\t1.- "+guests[0].title()+
    "\n\t2.- "+guests[1].title()+
    "\n\t3.- "+guests[2].title())

# Add a new line that prints a message saying that you can invite only 
# two people for dinner.
print("\nAhora solo se pueden invitar a dos personas a la cena...")

# Use pop() to remove guests from your list one at a time until only 
# two names remain in your list. 
# 
# Each time you pop a name from your list, print a message to that 
# person letting them know you’re sorry you can’t invite them to dinner.

cantity_to_delete = (2-len(guests))
cantity_to_delete = cantity_to_delete*-1 if cantity_to_delete<0 else cantity_to_delete

for index in range(cantity_to_delete):
    not_invited = guests.pop()
    print("Lo lamento, pero no podré invitarte a la cena "+not_invited.title())

# Print a message to each of the two people still on your list, letting 
# them know they’re still invited.
print("\nLas siguientes personas aún estan invitadas!")
for guest in guests:
    print("\t-"+guest.title())

# Use del to remove the last two names from your list, so you have an 
# empty list. Print your list to make sure you actually have an empty 
# list at the end of your program.
del guests[1]
del guests[0]

print("\n")
print(guests)
# 7-10. Dream Vacation: Write a program that polls users about their dream 
# vacation . Write a prompt similar to If you could visit one place in the world, 
# where would you go? Include a block of code that prints the results of the poll

responses = {

}

polling_active = True

while polling_active:
    name = input("\nPlease enter your name: ")
    responses[name] = input("If you could visit one place in the world, where would you go?: ")
    
    answer = input("Would you like to let another person reply? (Y/N)\n")
    if(answer.lower()=="n"):
        polling_active=False

print(" --- POLL RESULTS ---")
for name, place in responses.items():
    print(name.title()+" would like to go to "+place.title())
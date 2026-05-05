# 7-2. Restaurant Seating: Write a program that asks the user how many people 
# are in their dinner group . If the answer is more than eight, print a message say
# ing they’ll have to wait for a table . Otherwise, report that their table is ready.
prompt = "Hello! How many people are in your group for the dinner?\n"

cantity = input(prompt)

if int(cantity) > 8:
    print("Y'all need to wait for a table")
else:
    print("The table is ready!")

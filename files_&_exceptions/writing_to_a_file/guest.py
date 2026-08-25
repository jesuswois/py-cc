# 10-3. Guest: Write a program that prompts the user for their name. When they
# respond, write their name to a file called guest.txt.

input_name = input("Enter your name: ")

file_path = 'guest.txt'

with open(file_path,'w') as file_object:
    file_object.write(input_name)
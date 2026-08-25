# 10-4. Guest Book: Write a while loop that prompts users for their name. When
# they enter their name, print a greeting to the screen and add a line recording
# their visit in a file called guest_book.txt. Make sure each entry appears on a
# new line in the file.

file_path = 'guest_book.txt'

with open(file_path, 'w') as file_object:
    print("Manually filling guest book (Enter 0 to end)")
    input_name = 1
    while True:
        input_name = input("Enter guest's name: ")
        if input_name == '0':
            print("Exiting...")
            break
        file_object.write(f"{input_name}\n")

# 10-1. Learning Python: Open a blank file in your text editor and write a few
# lines summarizing what you’ve learned about Python so far. Start each line
# with the phrase In Python you can.... Save the file as learning_python.txt in the
# same directory as your exercises from this chapter. Write a program that reads
# the file and prints what you wrote three times. Print the contents once by read-
# ing in the entire file, once by looping over the file object, and once by storing
# the lines in a list and then working with them outside the with block.

file_path = "learning_python.txt"

with open(file_path) as file_object:
    content = file_object.read()
    print("\nReading the entire file with .read():"+content)

    file_object.seek(0) 
    # Seek is required because .read() reaches the end of the file, which causes any
    # future calls to it return an empty string. Seek re-positions the file object's position.

    print("\nReading the entire file by looping through the file object:")
    for line in file_object:
        print(line.rstrip()) 
    
    file_object.seek(0)

    lines = file_object.readlines()

print()

for line in lines:
    print(line.rstrip())
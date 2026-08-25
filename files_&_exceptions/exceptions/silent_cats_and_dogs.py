# 10-9. Silent Cats and Dogs: Modify your except block in Exercise 10-8 to fail
# silently if either file is missing.

cats_file = 'cats.txt'
dogs_file = 'dogs.txt'

def printFile(file_path):
    try:
        with open(file_path) as file_object:
            print("----start----")
            for line in file_object:
                print(line.rstrip())
            print("-----end-----\n")
    except FileNotFoundError:
        pass

print(f"Trying to read {cats_file}")
printFile(cats_file)
print(f"Trying to read {dogs_file}")
printFile(dogs_file)
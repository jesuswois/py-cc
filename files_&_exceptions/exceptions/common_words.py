# 10-10. Common Words: Visit Project Gutenberg (http://gutenberg.org/ )
# and find a few texts you’d like to analyze. Download the text files for these
# works, or copy the raw text from your browser into a text file on your
# computer.
# You can use the count() method to find out how many times a word or
# phrase appears in a string. For example, the following code counts the number
# of times 'row' appears in a string:
#   >>> line = "Row, row, row your boat"
#   >>> line.count('row')
#       2
#   >>> line.lower().count('row')
#       3
# Notice that converting the string to lowercase using lower() catches
# all appearances of the word you’re looking for, regardless of how it’s
# formatted.
# Write a program that reads the files you found at Project Gutenberg and
# determines how many times the word 'the' appears in each text.

def countOccurrences(file_path, word):
    try:
        with open(file_path, encoding='utf-8') as file_object:
            lines = file_object.readlines()
            word_count = 0
            for line in lines:
                word_count += line.lower().count(word)
            print(f"The word \"{word}\" is found exactly {word_count} times in the file \"{file_path}\"")
    except FileNotFoundError:
        print(f"The file {file_path} doesn't exist!")

file_path = 'proyect_gutenberg.txt'

countOccurrences(file_path,"the")
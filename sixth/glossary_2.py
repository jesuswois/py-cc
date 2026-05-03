# 6-4. Glossary 2: Now that you know how to loop through a dictionary, clean
# up the code from Exercise 6-3 (page 102) by replacing your series of print
# statements with a loop that runs through the dictionary’s keys and values.
# When you’re sure that your loop works, add five more Python terms to your
# glossary. When you run your program again, these new words and meanings
# should automatically be included in the output.

glossary = {
    "list":"The equivalent of an array in other languages. It allows the capacity to store multiple values in a variable.",
    "declaration":"Commonly refers to variable declarations.",
    "expression":"Something that evaluates to a value.",
    "conditional":"It's a python control flow, which is used to execute a block of code only if certain condition is True.",
    "dictionary":"It's a set key-value pair values."
}

for word,definition in glossary.items():
    print(word+"\n\t"+definition)
    print("\n")
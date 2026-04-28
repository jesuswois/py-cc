# 6-3. Glossary: A Python dictionary can be used to model an actual dictionary.
# However, to avoid confusion, let’s call it a glossary.
# • Think of five programming words you’ve learned about in the previous
# chapters. Use these words as the keys in your glossary, and store their
# meanings as values.
# • Print each word and its meaning as neatly formatted output. You might
# print the word followed by a colon and then its meaning, or print the word
# on one line and then print its meaning indented on a second line. Use the
# newline character (\n) to insert a blank line between each word-meaning
# pair in your output.

glossary = {
    "list":"The equivalent of an array in other languages. It allows the capacity to store multiple values in a variable.",
    "declaration":"Commonly refers to variable declarations.",
    "expression":"Something that evaluates to a value.",
    "conditional":"It's a python control flow, which is used to execute a block of code only if certain condition is True.",
    "dictionary":"It's a set key-value pair values."
}

for word in glossary:
    print(word+"\n\t"+glossary[word])
    print("\n")
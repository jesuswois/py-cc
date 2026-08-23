# 9-13. OrderedDict Rewrite: Start with Exercise 6-4 (page 108), where you
# used a standard dictionary to represent a glossary. Rewrite the program using
# the OrderedDict class and make sure the order of the output matches the order
# in which key-value pairs were added to the dictionary.

from collections import OrderedDict

glossary = OrderedDict()

glossary["list"] = "The equivalent of an array in other languages. It allows the capacity to store multiple values in a variable."
glossary["declaration"] = "Commonly refers to variable declarations."
glossary["expression"] = "Something that evaluates to a value."
glossary["conditional"] = "It's a python control flow, which is used to execute a block of code only if certain condition is True."
glossary["dictionary"] = "It's a set key-value pair values."

for word, definition in glossary.items():
    print(f"{word}\n\t{definition}\n")

# glossary = {
#     "list":"The equivalent of an array in other languages. It allows the capacity to store multiple values in a variable.",
#     "declaration":"Commonly refers to variable declarations.",
#     "expression":"Something that evaluates to a value.",
#     "conditional":"It's a python control flow, which is used to execute a block of code only if certain condition is True.",
#     "dictionary":"It's a set key-value pair values."
# }
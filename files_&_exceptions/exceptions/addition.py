# 10-6. Addition: One common problem when prompting for numerical input
# occurs when people provide text instead of numbers. When you try to convert
# the input to an int, you’ll get a TypeError. Write a program that prompts for
# two numbers. Add them together and print the result. Catch the TypeError if
# either input value is not a number, and print a friendly error message. Test your
# program by entering two numbers and then by entering some text instead of a
# number.

first_number = input("Enter the first number: ")
second_number = input("Enter the second number: ")

try:
    result = int(first_number) + int(second_number)
except ValueError:
    print("You've entered a value that's not a number.")
else:
    print(f"The sum of the given numbers is: {int(result)}")
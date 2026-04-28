import os

def clear():
    os.system("cls")

# 4-3. Counting to Twenty: Use a for loop to print the numbers from 1 to 20,
# inclusive.
for number in range(1,21):
    print(number)

input()
clear()
# 4-4. One Million: Make a list of the numbers from one to one million, and then
# use a for loop to print the numbers. (If the output is taking too long, stop it by
# pressing ctrl-C or by closing the output window.)

print("Print to 1 million?")
if(input()=="Y"):
    for number in range(1,1000001):
        print(number)
    input()

clear()

# 4-5. Summing a Million: Make a list of the numbers from one to one million,
# and then use min() and max() to make sure your list actually starts at one and
# ends at one million. Also, use the sum() function to see how quickly Python can
# add a million numbers.

million = range(1,1000001)
print("Min: "+str(min(million)))
print("Max: "+str(max(million)))

input()
clear()
# 4-6. Odd Numbers: Use the third argument of the range() function to make a list
# of the odd numbers from 1 to 20. Use a for loop to print each number.
odd_numbers = range(1,21,2)

for odd_number in odd_numbers:
    print(odd_number)

input()
clear()

# 4-7. Threes: Make a list of the multiples of 3 from 3 to 30. Use a for loop to
# print the numbers in your list.
multiples_of_three = [value*3 for value in range(1,11)]

for multiple_of_three in multiples_of_three:
    print(multiple_of_three)

input()
clear()

# 4-8. Cubes: A number raised to the third power is called a cube. For example,
# the cube of 2 is written as 2**3 in Python. Make a list of the first 10 cubes (that
# is, the cube of each integer from 1 through 10), and use a for loop to print out
# the value of each cube.
integers = range(1,11)

for integer in integers:
    integer = integer**3
    print(integer)

input()
clear()

# 4-9. Cube Comprehension: Use a list comprehension to generate a list of the
# first 10 cubes.

cubes = [value**3 for value in range(1,11)]

for cube in cubes:
    print(cube)
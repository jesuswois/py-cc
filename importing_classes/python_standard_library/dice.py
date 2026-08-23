# 9-14. Dice: The module random contains functions that generate random num-
# bers in a variety of ways. The function randint() returns an integer in the
# range you provide. The following code returns a number between 1 and 6:
# from random import randint
# x = randint(1, 6)
# Make a class Die with one attribute called sides, which has a default
# value of 6. Write a method called roll_die() that prints a random number
# between 1 and the number of sides the die has. Make a 6-sided die and roll
# it 10 times.
# Make a 10-sided die and a 20-sided die. Roll each die 10 times.

from random import randint

class Dice:    
    def __init__(self, sides = 6):
        self.sides = sides
    
    def roll_dice(self):
        print(randint(1,self.sides))

dice_6_sides = Dice()
dice_10_sides = Dice(10)
dice_20_sides = Dice(20)

print("\n6 Sides Dice's Rolls:")
for i in range(1,11):
    print(f"\t-Roll {i} = ",end='')
    dice_6_sides.roll_dice()

print("\n10 Sides Dice's Rolls:")
for i in range(1,11):
    print(f"\t-Roll {i} = ",end='')
    dice_10_sides.roll_dice()

print("\n20 Sides Dice's Rolls:")
for i in range(1,11):
    print(f"\t-Roll {i} = ",end='')
    dice_20_sides.roll_dice()
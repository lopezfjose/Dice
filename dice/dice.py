
import random

MAX_NUMBER_OF_ROLLS = 20
MAX_NUMBER_OF_DIE_FACES = 1000

EXIT_FAILURE = 1

class Die:
    def __init__(self, sides = 6, faces = [ 1, 2, 3, 4, 5, 6 ]):
        self.sides = sides
        self.faces = faces

    def roll(self):
        return random.choice(self.faces)

    def __str__(self):
        separator = ","

        sequence = []

        for face in self.faces:
            sequence.append(str(face))

        return separator.join(sequence)


def RollDice(n, dice):
    for i in range(n):
        print("Roll %d:" % (i + 1))
        for die in dice:
            print("\t%d" % die.roll())

def EnterNumberOfDiceRolls():
    n = int(input("Please enter the number of times you would like to roll the dice: "))

    if n < 1:
        print("The number of dice rolls must be greater than 1.")
        exit(EXIT_FAILURE)

    if n > MAX_NUMBER_OF_ROLLS:
        print("The number of dice rolls must be less than %d." % MAX_NUMBER_OF_ROLLS)
        exit(EXIT_FAILURE)

    return n

def SetNumberOfDieFaces():
    n = int(input("Please enter the number of faces the die will have: "))

    if n < 2:
        print("The die must have at least 2 faces.")
        exit(EXIT_FAILURE)
    elif n >= MAX_NUMBER_OF_DIE_FACES:
        print("The die must have less than %d faces." % MAX_NUMBER_OF_DIE_FACES)
        exit(EXIT_FAILURE)

    return n

def SetDieFaces(numberOfSides):
    dieFaces = []

    for face in dieFaces:
        dieFaces.append(input("Side 1: "))

    return dieFaces

def SetDiceToRoll(dice):
    diceToRoll = []

    for die in dice:
        diceToRoll.append(die)

    return diceToRoll

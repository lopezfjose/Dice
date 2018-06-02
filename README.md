
Dice
=========

This is just a basic hobby project I made because I couldn't really find any options that had the features and complexity I wanted, let alone the intuitive interface and accessiblity, so here we are. Feel free to drop me a line if you have a feature request, bug fix, etc.

Basic Example
=============

```pythonstub
import dice

sixSidedDie = dice.Die()

print("Die: ", sixSidedDie)

numberOfTimesToRollDice = dice.EnterNumberOfDiceRolls()

dice.RollDice(numberOfTimesToRollDice, [sixSidedDie, sixSidedDie])
```

Output
--

```
Die:  1,2,3,4,5,6
Please enter the number of times you would like to roll the dice: 4
Roll 1:
	5
	5
Roll 2:
	2
	5
Roll 3:
	3
	3
Roll 4:
	1
	5
```

Creating Custom Die
=====================

```pythonstub
import dice

newDieSides             = dice.SetNumberOfDieFaces()
newDieFaces             = dice.SetDieFaces(newDieSides)
newDie                  = dice.Die()
numberOfTimesToRollDice = dice.EnterNumberOfDiceRolls()
diceToRoll              = dice.SetDiceToRoll([newDie, newDie, newDie])
dice.RollDice(numberOfTimesToRollDice, diceToRoll)
```

Command Line Options
====================

```commandline
python main.py --config="default.cfg"
```
Output
```commandline
Configuration file: default.cfg
```


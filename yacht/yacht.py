"""
This exercise stub and the test suite contain several enumerated constants.

Since Python 2 does not have the enum module, the idiomatic way to write
enumerated constants has traditionally been a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it’s memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""


# Score categories.
# Change the values as you see fit.
YACHT = 50
ONES = 1
TWOS = 2
THREES = 3
FOURS = 4
FIVES = 5
SIXES = 6
FULL_HOUSE = None
FOUR_OF_A_KIND = None
LITTLE_STRAIGHT = 30
BIG_STRAIGHT = 30
CHOICE = None


def score(dice, category):
    num_counts = [(i, dice.count(i)) for i in set(dice)]
    sort_counts = sorted([y for x, y in num_counts])

    if category == YACHT and all(x == dice[0] for x in dice):
        score = YACHT
    elif category == FOUR_OF_A_KIND:
        score = sum([x*4 for x, y in num_counts if y >= 4])
    elif category == CHOICE:
        score = sum(dice)
    elif category == BIG_STRAIGHT and dice == [2,3,4,5,6]:
        score = BIG_STRAIGHT
    elif category == LITTLE_STRAIGHT and dice == [1,2,3,4,5]:
        score = LITTLE_STRAIGHT
    elif category == FULL_HOUSE and sort_counts == [2,3]:
        score = sum([x*y for x, y in num_counts])
    else:
        score = dice.count(category)*category
    return score
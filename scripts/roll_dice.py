"""
roll_dice.py
Get a random dice roll.
"""

__all__ = []

import time
import random

from sense_hat import SenseHat

sense = SenseHat()
sense.rotation = 90


class Dice(object):
    """A Dice with random rolls.
    Generatated using ambient humidity and temperature readings from he
    ense hat sensors.
    """

    o = (0, 0, 0)
    x = (255, 255, 255)

    border = (
        x, x, x, x, x, x, x, x,
        x, o, o, o, o, o, o, x,
        x, o, o, o, o, o, o, x,
        x, o, o, o, o, o, o, x,
        x, o, o, o, o, o, o, x,
        x, o, o, o, o, o, o, x,
        x, o, o, o, o, o, o, x,
        x, x, x, x, x, x, x, x,
    )

    def __init__(self):
        """init"""
        self.one = (19, 20, 26, 27, 28, 29, 34, 35, 36, 37, 43, 44)
        self.two = (9, 10, 17, 18, 45, 46, 53, 54)
        self.three = (9, 10, 17, 18, 27, 28, 35, 36, 45, 46, 53, 54)
        self.four = (
        9, 10, 17, 18, 13, 14, 21, 22, 41, 42, 49, 50, 45, 46, 53, 54)
        self.five = (
        9, 10, 17, 18, 13, 14, 21, 22, 41, 42, 49, 50, 27, 28, 35, 36, 45, 46,
        53, 54)
        self.six = (
        9, 10, 17, 18, 13, 14, 21, 22, 25, 26, 33, 34, 29, 30, 37, 38, 41, 42,
        49, 50, 45, 46, 53, 54)
        self.result = None

    def show(self, number):
        """Display the dice roll to the LED grid."""
        die_numbers = (
        self.one, self.two, self.three, self.four, self.five, self.six)
        die_face = list(self.border)

        for n in die_numbers[number - 1]:
            if number == 1:
                die_face[n] = (255, 0, 0)
            else:
                die_face[n] = (0, 255, 0)

        sense.set_pixels(die_face)

    def roll(self):
        """Generate a random dice roll."""
        self.result = random.randint(0, 6)
        if self.result == 0:
            self.result = 6

        self.show(self.result)


def roll_dice():
    """Roll the dice."""
    sense.clear()
    dice = Dice()

    for i in range(random.randrange(10, 41)):
        dice.show(random.randrange(1, 7))

    for i in range(random.randrange(10, 31)):
        dice.show(random.randrange(1, 7))
        time.sleep(0.1)

    for i in range(random.randrange(10, 21)):
        dice.show(random.randrange(1, 7))
        time.sleep(0.2)

    for i in range(random.randrange(10, 11)):
        dice.roll()
        time.sleep(random.random())

    if dice.result == 1:
        message = 'aha, bullseye!'
    else:
        message = 'it\'s ' + str(dice.result)

    print('roll_dice', message)
    time.sleep(2)


if __name__ == '__main__':
    roll_dice()
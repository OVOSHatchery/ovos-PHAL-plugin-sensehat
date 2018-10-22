from sense_hat import SenseHat
import time

sense = SenseHat()

sense.clear()

r = 0
g = 0
b = 0
colour_value = 0

while colour_value < 16581375:
    print(colour_value)
    O = [r, g, b]
    rgb_showcase = [
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O
    ]
    sense.set_pixels(rgb_showcase)
    colour_value = colour_value + 1
    r = r + 1

    if r == 255:
        r = 0
        g = g + 1
    if g == 255:
        g = 0
        b = b + 1
    if b == 255:
        r = 0
        g = 0
        b = 0

    sense.set_pixels(rgb_showcase)

else:
    sense.show_message("You have reached " + str(colour_value),
                       text_colour=[255, 255, 255])

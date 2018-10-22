# twinkling tree
import time
from sense_hat import SenseHat

sense = SenseHat()
tree = [(0, 0, 64), (0, 0, 64), (0, 0, 64), (0, 0, 64), (0, 0, 64), (0, 0, 64),
        (0, 0, 64), (0, 0, 64), (0, 0, 64), (0, 0, 64), (0, 0, 64),
        (32, 64, 64), (32, 64, 64), (0, 0, 64), (0, 0, 64), (0, 0, 64),
        (0, 0, 64), (0, 0, 64), (32, 64, 64), (32, 64, 64), (32, 64, 64),
        (32, 64, 64), (0, 0, 64), (0, 0, 64), (0, 0, 48), (0, 0, 48),
        (32, 64, 64), (32, 64, 64), (32, 64, 64), (32, 64, 64), (0, 0, 48),
        (0, 0, 48), (0, 0, 48), (32, 64, 64), (32, 64, 64), (32, 64, 64),
        (32, 64, 64), (32, 64, 64), (32, 64, 64), (0, 0, 48), (0, 0, 48),
        (32, 64, 64), (32, 64, 64), (64, 128, 128), (64, 128, 128),
        (32, 64, 64), (32, 64, 64), (0, 0, 48), (0, 0, 0), (32, 64, 64),
        (32, 64, 64), (64, 128, 128), (64, 128, 128), (32, 64, 64),
        (32, 64, 64), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0),
        (64, 128, 128), (64, 128, 128), (0, 0, 0), (0, 0, 0), (0, 0, 0)]
sense.set_pixels(tree)


def twinkle(count, interval):
    m = count % interval
    if (m <= 3):  # from 0 to 3
        rg = m * 20 + 195
        b = m * 80 + 15
        return (rg, rg, b)
    elif (m < 6):  # from 4 to 6
        rg = (6 - m) * 20 + 195
        b = (6 - m) * 80 + 15
        return (rg, rg, b)
    else:
        return (195, 195, 0)


count = 50;
while True:
    time.sleep(0.1)
    # star at the top
    #
    tree[3] = twinkle(count, 37)
    tree[11] = twinkle(count, 37)
    tree[10] = twinkle(count, 37)
    tree[12] = twinkle(count, 37)
    tree[19] = twinkle(count, 37)
    # small stars
    #
    tree[26] = twinkle(count, 29)
    tree[29] = twinkle(count, 21)
    tree[41] = twinkle(count, 19)
    tree[44] = twinkle(count, 16)
    sense.set_pixels(tree)
    count += 1
    if (count > 10 * 16 * 21 * 29 * 37):
        count = 0
    # print(count)

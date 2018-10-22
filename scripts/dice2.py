import random
from time import sleep
from sense_hat import SenseHat

sense = SenseHat()
sense.set_imu_config(False, False, True)

O = [0, 0, 0]   #sets the background color
X = [0, 0, 90]  #sets the dot color

# sets images for each number
one = [
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        O, O, O, X, X, O, O, O,
        O, O, O, X, X, O, O, O,
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O
        ]
two = [
        X, X, O, O, O, O, O, O,
        X, X, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, X, X,
        O, O, O, O, O, O, X, X
        ]
thr = [
        X, X, O, O, O, O, O, O,
        X, X, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        O, O, O, X, X, O, O, O,
        O, O, O, X, X, O, O, O,
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, X, X,
        O, O, O, O, O, O, X, X
        ]
fou = [
        X, X, O, O, O, O, X, X,
        X, X, O, O, O, O, X, X,
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        X, X, O, O, O, O, X, X,
        X, X, O, O, O, O, X, X
        ]
fiv = [
        X, X, O, O, O, O, X, X,
        X, X, O, O, O, O, X, X,
        O, O, O, O, O, O, O, O,
        O, O, O, X, X, O, O, O,
        O, O, O, X, X, O, O, O,
        O, O, O, O, O, O, O, O,
        X, X, O, O, O, O, X, X,
        X, X, O, O, O, O, X, X
        ]
six = [
        X, X, O, O, O, O, X, X,
        X, X, O, O, O, O, X, X,
        O, O, O, O, O, O, O, O,
        X, X, O, O, O, O, X, X,
        X, X, O, O, O, O, X, X,
        O, O, O, O, O, O, O, O,
        X, X, O, O, O, O, X, X,
        X, X, O, O, O, O, X, X
        ]
# creates the roll dice functions and iterates 500 random numbers before stopping giving the visualization it's 'rolling'
def roll_dice():
    i =0
    while (i < 500):
        sense.clear()
        num_img = [one, two, thr, fou, fiv, six]        #set the images in a list
        dice_num = random.randint(0,5)                  #generates random number between 0-5
        sense.set_pixels(num_img[dice_num])             #uses random number to pull from image list
        i += 1 #interates i

#uses the accelerometer sensors to intiated the roll dice function
while True:
    x, y, z, = list(sense.get_accelerometer_raw().values())

    x, y, z = abs(x), abs(y), abs(z) #set x y and z values to absolute values

    if x > 1.4 or y > 1.4 or z > 1.4:
        roll_dice()
        sleep(3)        #shows the dice/dots for 3 seconds before clearing the screen
        sense.clear() #rests the leds
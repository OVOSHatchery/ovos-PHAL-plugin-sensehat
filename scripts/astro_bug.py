#!/usr/bin/python3
import time, math, random
import sense_hat

"""

  Astro Bug!

  A bug game.  Eat the food! Avoid the enemies!

  Modify the starting state in the `state` dict.

  Note: Requires sense_hat version 2.2.0 or later.

"""

starting_enemies = [[4, 6], [0, 4]]

state = {"bug_x": 4,
         "bug_y": 4,
         "bug_rgb": (250, 250, 250),
         "food_x": 2,
         "food_y": 7,
         "food_rgb": (0, 255, 50),
         "level": 1,
         "enemies": starting_enemies,
         "enemy_rgb": (255, 50, 0)}

start_over_state = dict(state)

sense = sense_hat.SenseHat()
sense.low_light = True


def setscreen():
    """Takes x and y vales and alters screen state. Does not
    modify state."""
    bug_x = state["bug_x"]
    bug_y = state["bug_y"]
    bug_rgb = state["bug_rgb"]
    food_x = state["food_x"]
    food_y = state["food_y"]
    food_rgb = state["food_rgb"]
    enemies = state["enemies"]
    enemy_rgb = state["enemy_rgb"]

    if sense.low_light:
        zero = 8
    else:
        zero = 48
    brightness = 255 - zero
    sense.clear((50, 100, 150))
    sense.set_pixel(food_x, food_y, food_rgb)
    sense.set_pixel(bug_x, bug_y, bug_rgb)
    for e in enemies:
        sense.set_pixel(e[0], e[1], enemy_rgb)


def distance(x1, y1, x2, y2):
    """returns distance of two points"""
    return math.hypot(x2 - x1, y2 - y1)


def clip(pixels, nmin=0, nmax=255):
    """Ensures rgb values are between 0 and 255"""
    return tuple(max(min(nmax, n), nmin) for n in pixels)


def check_pos():
    """Checks for eating food and hitting enemies. Alters state but
    does not redraw screen.  Call setscreen() after this."""
    global state
    bug_x = state["bug_x"]
    bug_y = state["bug_y"]
    food_x = state["food_x"]
    food_y = state["food_y"]
    level = state["level"]
    enemies = state["enemies"]

    weaker = int(10 * (level / 2))
    stronger = 10
    radius = 2.5
    fdist = distance(bug_x, bug_y, food_x, food_y)

    for e in enemies:
        edist = distance(bug_x, bug_y, e[0], e[1])
        if edist == 0:
            # Hit an enemy; game over & reset
            sense.show_message("R.I.P. Bug, Level {0}".format(state["level"]))
            state = dict(start_over_state)
            return

    if fdist > radius:
        # Bug is far away; grow weaker
        state["bug_rgb"] = clip([abs(i - weaker) for i in state["bug_rgb"]])
    elif fdist == 0.0:
        # Bug ate food and is healthy again
        state["bug_rgb"] = (255, 255, 255)
        state["level"] += 1
        state["enemies"] += [[random.randint(0, 7), random.randint(0, 7)]]
        sense.show_message(str(state["level"]))
        time.sleep(1)
        # Set food to new location that's not under the bug
        while True:
            state["food_x"] = random.randint(0, 7)
            if state["food_x"] != state["bug_x"]:
                break
        while True:
            state["food_y"] = random.randint(0, 7)
            if state["food_y"] != state["bug_y"]:
                break
    elif fdist < radius:
        # Bug is close; grow a little stronger
        state["bug_rgb"] = clip([abs(i + stronger) for i in state["bug_rgb"]])


def rand_step(xy):
    """Returns one iteration of a random walk of x,y coordinates"""
    x, y = xy

    new_x = x + random.choice([-1, 0, 1])
    new_y = y + random.choice([-1, 0, 1])
    return [0 if new_x == 8 else 7 if new_x == -1 else new_x, \
            0 if new_y == 8 else 7 if new_y == -1 else new_y]


def move_enemies():
    global state
    enemies = state["enemies"]
    reserved = [[state["bug_x"], state["bug_y"]],
                [state["food_x"], state["food_y"]]]
    new_enemies = []
    for e in enemies:
        while True:
            new_e = rand_step(e)
            if new_e not in reserved:
                break
        new_enemies.append(new_e)
    state["enemies"] = new_enemies
    setscreen()


def draw_bug(event):
    """Takes a keypress and redraws the screen"""
    global state
    if event.action == sense_hat.ACTION_RELEASED:
        # Ignore releases
        return
    elif event.direction == sense_hat.DIRECTION_UP:
        state["bug_x"] = state["bug_x"]
        state["bug_y"] = 7 if state["bug_y"] == 0 else state["bug_y"] - 1
    elif event.direction == sense_hat.DIRECTION_DOWN:
        state["bug_x"] = state["bug_x"]
        state["bug_y"] = 0 if state["bug_y"] == 7 else state["bug_y"] + 1
    elif event.direction == sense_hat.DIRECTION_RIGHT:
        state["bug_x"] = 0 if state["bug_x"] == 7 else state["bug_x"] + 1
        state["bug_y"] = state["bug_y"]
    elif event.direction == sense_hat.DIRECTION_LEFT:
        state["bug_x"] = 7 if state["bug_x"] == 0 else state["bug_x"] - 1
        state["bug_y"] = state["bug_y"]

        # Check to see if anything should happen
    setscreen()
    check_pos()
    setscreen()


# Initial state
setscreen()
sense.set_pixel(state["bug_x"], state["bug_y"], state["bug_rgb"])

last_tick = round(time.time(), 1) * 10

while True:
    # Enemies move faster in higher levels
    timer = 20 - (state["level"] % 20)

    # Every so often, move enemies
    tick = round(time.time(), 1) * 10
    if (tick % timer == 0) and (tick > last_tick):
        move_enemies()
        last_tick = tick

    # Poll joystick for events. When they happen, redraw screen.
    for event in sense.stick.get_events():
        draw_bug(event)
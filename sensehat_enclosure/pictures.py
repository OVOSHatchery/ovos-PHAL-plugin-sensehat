G = green = (0, 255, 0)
LG = light_green = (198, 247, 51)
Y = yellow = (255, 255, 0)
B = blue = (0, 0, 255)
BB = bright_blue = (111, 225, 226)
R = red = (255, 0, 0)
LR = light_red = (256, 111, 111)
W = X = white = (255, 255, 255)
A = amber = (255, 140, 0)
N = O = off = nothing = (0, 0, 0)
pink = (255, 105, 180)
light_pink = (249, 157, 209)
P = purple = (155, 0, 255)
LP = light_purple = (249, 132, 249)
I = indigo = (111, 0, 255)
V = violet = (159, 0, 255)

tree = [
    B, B, B, R, R, B, B, B,
    B, B, G, G, G, G, B, B,
    B, R, G, G, G, G, R, B,
    B, G, G, G, G, G, G, B,
    R, G, G, G, G, G, G, R,
    G, G, G, G, G, G, G, G,
    B, B, B, G, G, B, B, B,
    B, B, B, G, G, B, B, B
]

question_mark = [
    O, O, O, X, X, O, O, O,
    O, O, X, O, O, X, O, O,
    O, O, O, O, O, X, O, O,
    O, O, O, O, X, O, O, O,
    O, O, O, X, O, O, O, O,
    O, O, O, X, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, X, O, O, O, O,
]

off = [
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
]

hearth = [
    P, P, P, O, O, P, P, P,
    P, P, P, P, P, P, P, P,
    P, P, P, P, P, P, P, P,
    O, P, P, P, P, P, P, O,
    O, O, P, P, P, P, O, O,
    O, O, O, P, P, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
]

happy_face = [
    O, O, O, O, O, O, O, O,
    O, G, G, O, O, G, G, O,
    O, G, G, O, O, G, G, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, G, O, O, O, O, G, O,
    O, O, G, G, G, G, O, O,
    O, O, O, O, O, O, O, O,
]

sad_face = [
    O, O, O, O, O, O, O, O,
    O, R, O, O, O, O, R, O,
    O, R, R, O, O, R, R, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, R, R, R, R, O, O,
    O, R, O, O, O, O, R, O,
    O, O, O, O, O, O, O, O,
]

building = [
    O, O, O, O, O, O, O, O,
    O, O, R, R, R, R, O, O,
    R, R, A, A, A, A, R, R,
    R, A, Y, Y, Y, Y, A, R,
    R, A, Y, G, G, Y, A, R,
    R, A, Y, G, G, Y, A, R,
    R, A, Y, G, G, Y, A, R,
    R, A, Y, G, G, Y, A, R,
]

scene = [
    Y, Y, B, Y, B, B, B, B,
    Y, Y, B, B, B, B, B, B,
    B, B, B, Y, B, B, B, B,
    R, Y, R, R, R, R, R, R,
    R, R, R, R, R, P, R, R,
    R, R, R, R, R, G, R, R,
    R, R, R, R, R, G, R, R,
    G, G, G, G, G, G, G, G,
]

cross = [
    O, R, O, O, O, O, R, O,
    R, R, R, O, O, R, R, R,
    O, R, R, R, R, R, R, O,
    O, O, R, R, R, R, O, O,
    O, O, R, R, R, R, O, O,
    O, R, R, R, R, R, R, O,
    R, R, R, O, O, R, R, R,
    O, R, O, O, O, O, R, O
]

neutral_face = [
    O, O, Y, Y, Y, Y, O, O,
    O, Y, O, O, O, O, Y, O,
    Y, O, Y, O, O, Y, O, Y,
    Y, O, O, O, O, O, O, Y,
    Y, O, O, O, O, O, O, Y,
    Y, O, Y, Y, Y, Y, O, Y,
    O, Y, O, O, O, O, Y, O,
    O, O, Y, Y, Y, Y, O, O
]

smile_face = [
    O, O, G, G, G, G, O, O,
    O, G, O, O, O, O, G, O,
    G, O, G, O, O, G, O, G,
    G, O, O, O, O, O, O, G,
    G, O, G, O, O, G, O, G,
    G, O, O, G, G, O, O, G,
    O, G, O, O, O, O, G, O,
    O, O, G, G, G, G, O, O
]

green_check = [
    N, N, N, N, N, N, N, G,
    N, N, N, N, N, N, G, G,
    N, N, N, N, N, G, G, G,
    N, N, N, N, N, G, G, N,
    N, G, N, N, G, G, G, N,
    G, G, G, N, G, G, N, N,
    N, G, G, G, G, N, N, N,
    N, N, G, G, G, N, N, N
]

button_off = [
    N, N, N, N, N, N, N, N,
    N, N, N, N, R, N, N, N,
    N, N, R, N, R, N, R, N,
    N, R, N, N, R, N, N, R,
    N, R, N, N, N, N, N, R,
    N, N, R, N, N, N, R, N,
    N, N, N, R, R, R, N, N,
    N, N, N, N, N, N, N, N
]

button_on = [
    N, N, N, N, N, N, N, N,
    N, N, N, N, G, N, N, N,
    N, N, G, N, G, N, G, N,
    N, G, N, N, G, N, N, G,
    N, G, N, N, N, N, N, G,
    N, N, G, N, N, N, G, N,
    N, N, N, G, G, G, N, N,
    N, N, N, N, N, N, N, N
]

raspi = [
    O, G, G, O, O, G, G, O,
    O, O, G, G, G, G, O, O,
    O, O, R, R, R, R, O, O,
    O, R, R, R, R, R, R, O,
    R, R, R, R, R, R, R, R,
    R, R, R, R, R, R, R, R,
    O, R, R, R, R, R, R, O,
    O, O, R, R, R, R, O, O,
]

plus = [
    O, O, O, O, O, O, O, O,
    O, O, O, W, W, O, O, O,
    O, O, O, W, W, O, O, O,
    O, W, W, W, W, W, W, O,
    O, W, W, W, W, W, W, O,
    O, O, O, W, W, O, O, O,
    O, O, O, W, W, O, O, O,
    O, O, O, O, O, O, O, O,
    ]

equals = [
    O, O, O, O, O, O, O, O,
    O, W, W, W, W, W, W, O,
    O, W, W, W, W, W, W, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, W, W, W, W, W, W, O,
    O, W, W, W, W, W, W, O,
    O, O, O, O, O, O, O, O,
    ]
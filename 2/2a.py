ROCK = 1
PAPER = 2
SCISSORS = 3

WIN_POINTS = 6
DRAW_POINTS = 3
LOSS_POINTS = 0

col_map = {
    'A': ROCK,
    'B': PAPER,
    'C': SCISSORS,
    'X': ROCK,
    'Y': PAPER,
    'Z': SCISSORS
}

def get_result(col_1, col_2):
    if col_1 == col_2:
        return DRAW_POINTS
    elif col_1 == ROCK:
        return WIN_POINTS if col_2 == PAPER else LOSS_POINTS
    elif col_1 == PAPER:
        return WIN_POINTS if col_2 == SCISSORS else LOSS_POINTS
    elif col_1 == SCISSORS:
        return WIN_POINTS if col_2 == ROCK else LOSS_POINTS  

with open('input.txt', 'r') as f:
    rounds = [
        tuple(
            col_map[r]
            for r in x.strip().split(' ')
        )
        for x in f.readlines()
    ]

points = [
    col[1] + get_result(col[0], col[1])
    for col in rounds
]

print(sum(points))

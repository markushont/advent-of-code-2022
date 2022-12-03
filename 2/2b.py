ROCK = 'rock'
PAPER = 'paper'
SCISSORS = 'scissors'

class Move:
    def __init__(self, beats, loses_to):
        # self.self = _self
        self.beats = beats
        self.loses_to = loses_to

        
class Rock(Move):
    points = 1
    def __init__(self):
        super().__init__(Scissors, Paper)

class Paper(Move):
    points = 2
    def __init__(self):
        super().__init__(Rock, Scissors)

class Scissors(Move):
    points = 3
    def __init__(self):
        super().__init__(Paper, Rock)

WIN_POINTS = 6
DRAW_POINTS = 3
LOSS_POINTS = 0

WIN = 'win'
LOSS = 'loss'
DRAW = 'draw'

col_1_map = {
    'A': Rock(),
    'B': Paper(),
    'C': Scissors()
}

col_2_map = {
    'X': LOSS,
    'Y': DRAW,
    'Z': WIN
}

def get_result(col_1, col_2):
    if type(col_1) == type(col_2):
        return DRAW_POINTS
    if type(col_2) == type(col_1.loses_to()):
        return WIN_POINTS
    if type(col_2) == type(col_1.beats()):
        return LOSS_POINTS
    raise Exception(':(')
    
def get_move(col_1, outcome):
    if outcome == DRAW:
        return col_1
    if outcome == WIN:
        return col_1.loses_to()
    elif outcome == LOSS:
        return col_1.beats()

with open('input.txt', 'r') as f:
    rounds = []
    for line in f.readlines():
        cols = line.strip().split(' ')
        col_1 = col_1_map[cols[0]]
        col_2 = col_2_map[cols[1]]
        rounds.append(
            (
                col_1,
                get_move(col_1, col_2)
            )
        )

points = [
    col[1].points + get_result(col[0], col[1])
    for col in rounds
]

print(sum(points))

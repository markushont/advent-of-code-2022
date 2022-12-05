from collections import deque
import re

class Move:
    def __init__(self, n, move_from, move_to):
        self.n = n
        self.move_from = move_from
        self.move_to = move_to


def make_move(line):
    patt = 'move (\d+?) from (\d+?) to (\d+?)'
    res = re.match(patt, line)
    return Move(
        int(res.group(1)),
        int(res.group(2)) - 1,
        int(res.group(3)) - 1
    )

def make_crates(lines):
    n_columns = 9
    crates = [deque() for _ in range(n_columns)]
    get_letter = lambda slot: slot[1] if slot[1] != ' ' else None
    for level in lines:
        for i in range(n_columns):
            letter = get_letter(level[i*4:i*4+4])
            if letter:
                crates[i].append(letter)
    return crates

with open('input.txt', 'r') as f:
    lines = deque([x.strip('\n') for x in f.readlines()])
    
crates_lines = deque()
line = lines.popleft()
while line:
    if line != ' 1   2   3   4   5   6   7   8   9 ':
        crates_lines.appendleft(line)
    line = lines.popleft()

crates = make_crates(crates_lines)

moves = [make_move(l) for l in lines]

for move in moves:
    for n in range(move.n):
        to_move = crates[move.move_from].pop()
        crates[move.move_to].append(to_move)

result = [crate[-1] for crate in crates]
print(''.join(result))

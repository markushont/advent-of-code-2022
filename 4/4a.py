with open('input.txt', 'r') as f:
    lines = [x.strip() for x in f.readlines()]


def get_range(range_str):
    interval = range_str.split('-')
    return set(range(
            int(interval[0]),
            int(interval[1]) + 1
        ))


lines = [
    (get_range(x.split(',')[0]), get_range(x.split(',')[1]))
    for x in lines
]

lines_filtered = [
    x
    for x in lines
    if x[0].issubset(x[1]) or x[1].issubset(x[0])
]

print(len(lines), len(lines_filtered))

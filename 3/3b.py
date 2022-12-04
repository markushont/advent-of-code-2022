import string

with open('input.txt', 'r') as f:
    lines = [x.strip() for x in f.readlines()]

    groups = [
        (lines[i], lines[i+1], lines[i+2])
        for i in range(0, len(lines), 3)
    ]

types = []
for group in groups:
    intersection = set(group[0])\
            .intersection(set(group[1]))\
            .intersection(set(group[2]))
    
    types += list(intersection)

priorities = {
    char: idx + 1
    for idx, char in enumerate(string.ascii_lowercase + string.ascii_uppercase)
}

points = [priorities[x] for x in types]

print(sum(points))

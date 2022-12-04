import string

with open('input.txt', 'r') as f:
    inp = [x.strip() for x in f.readlines()]

    lines = [(x[:int(len(x)/2)], x[int(len(x)/2):]) for x in inp]


priorities = {
    char: idx + 1
    for idx, char in enumerate(string.ascii_lowercase + string.ascii_uppercase)
}

types = set()
types_arr = []
for comps in lines:
    comp_1 = set(comps[0])
    comp_2 = set(comps[1])

    intersection = comp_1.intersection(comp_2)

    types.update(intersection)
    types_arr += list(intersection)

points = [priorities[x] for x in types]
arr_points = [priorities[x] for x in types_arr]

# print(types)
# print(points)
print(sum(points))
print(sum(arr_points))
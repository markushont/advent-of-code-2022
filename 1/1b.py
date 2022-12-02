

with open('input.txt', 'r') as f:
    lines = [l.strip() for l in f.readlines()]


buckets = {}

elve_count = 0
for line in lines:
    if line == '' or len(line) == 0:
        elve_count += 1
        continue

    if elve_count not in buckets:
        buckets[elve_count] = int(line.strip())
    else:
        buckets[elve_count] += int(line.strip())


sorted_buckets = sorted([v for _,v in buckets.items()], reverse=True)

print(sum(sorted_buckets[:3]))

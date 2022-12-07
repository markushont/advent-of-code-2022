from collections import deque

with open('input.txt', 'r') as f:
    line = f.readlines()[0].strip()

def get_res():
    buf = deque()
    for i in range(len(line)):
        if len(buf) == 14:
            if len(set(buf)) == 14:
                return i
            buf.popleft()
        buf.append(line[i])

res = get_res()
print(res)

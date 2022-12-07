from collections import deque

with open('input.txt', 'r') as f:
    line = f.readlines()[0].strip()

def get_res():
    buf = deque()
    for i in range(len(line)):
        if len(buf) == 4:
            if len(set(buf)) == 4:
                return i
                # seen = ''
                # for j in range(3, 0, -1):
                #     if buf[j] in seen:
                #         print(buf, i, j)
                #         return i - (3 - j)
                #     seen += buf[j]
            buf.popleft()
        buf.append(line[i])

res = get_res()
print(res)

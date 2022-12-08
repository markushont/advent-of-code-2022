import re

class File:
    def __init__(self, path, size, name):
        self.path = path
        self.size = int(size)
        self.name = name

with open('input.txt', 'r') as f:
    lines = [x.strip() for x in f.readlines()[1:]]

current_path = ['root']
files = {}
for line in lines:
    cd_res = re.match('^\$ cd (.*?)$', line)
    if cd_res:
        tgt = cd_res.group(1)
        if tgt == '..':
            current_path.pop()
        else:
            current_path.append(tgt)
        
        continue

    current_path_str = '/'.join(current_path)
    if current_path_str not in files:
        files[current_path_str] = []

    if line == '$ ls':
        continue

    if line.startswith('dir '):
        continue

    file_info = line.split(' ')
    files[current_path_str].append(File(current_path_str, file_info[0], file_info[1]))

dirs = list(files.keys())
sizes = {}
for dir in dirs:
    size = 0
    for subdir in [x for x in dirs if x.startswith(dir)]:
        size += sum(x.size for x in files[subdir])
    sizes[dir] = size

sort = sorted(sizes.values())

total_disk_size = 70000000
required_space = 30000000
space_unused = total_disk_size - max(sort)

print(next(x for x in sort if x > required_space - space_unused))
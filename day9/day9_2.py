densemap = [int(x) for x in input().strip()]

files = []
spaces = []
diskmap = []

class Space:
    def __init__(self, pos, size):
        self.pos = pos
        self.size = size

pos = 0
for i, x in enumerate(densemap):
    if i % 2 == 0:
        files.append((i//2, pos, x))
        diskmap += [i // 2] * x
    else:
        diskmap += [None] * x
        spaces.append(Space(pos, x))
    pos += x

while files:
    fid, fpos, fsize = files.pop()
    for s in spaces:
        if s.pos > fpos:
            break
        if s.size >= fsize:
            for i in range(fsize):
                diskmap[s.pos + i] = fid
                diskmap[fpos + i] = None
            s.size -= fsize
            s.pos += fsize
            break
print(sum([i * (diskmap[i] or 0) for i in range(len(diskmap))]))

densemap = [int(x) for x in input().strip()]

diskmap = []
fileslen = 0
for i, x in enumerate(densemap):
    if i % 2 == 0:
        diskmap += [i // 2] * x
        fileslen += x
    else:
        diskmap += [None] * x

s = 0
pos = 0
endpos = len(diskmap) - 1
while endpos > -1  and diskmap[endpos] is None:
    endpos -= 1 
while pos < fileslen:
    if diskmap[pos] is None and endpos > -1:
        diskmap[pos] = diskmap[endpos]
        endpos -= 1
        while endpos > -1  and diskmap[endpos] is None:
            endpos -= 1 
    s += pos * (diskmap[pos] or 0)
    pos += 1
print(s)

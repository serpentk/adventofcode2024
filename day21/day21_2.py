import sys
import collections

STEPS = 24
STEPS = 3


class BaseKeyboard:
    buttons = {}

    def get_sequence(self, input_seq):
        curx, cury = self.buttons['A']
        res = []
        for c in input_seq:
            x, y = self.buttons[c]
            dx = []
            if x < curx:
                dx = ['^'] * (curx - x)
            elif x > curx:
                dx = ['V'] * (x - curx)
            # if y < cury:
            #     dy = '<' * (cury - y)
            # elif y > cury:
            #     dy = '>' * (y - cury)
            
            if y >= cury:
                if (curx, y) not in self.buttons.values():
                    print('Oooops {} cur {} target{}'.format(input_seq, (curx, cury), (x, y)))
                    print(self.buttons)
                    exit(1)
                res += ['>'] * (y - cury) + dx + ['A']
            else:
                if (x, cury) not in self.buttons.values():
                    print('Oooops {} cur {} target {}'.format(input_seq, (curx, cury), (x, y)))
                    print(self.buttons)
                    exit(1)
                res += dx + ['<'] * (cury - y) + ['A']
            curx, cury = x, y
        return ''.join(res)
                
    def exec_sequence(self, input_seq):
        inv_buttons = {v: k for k, v in self.buttons.items()}
        curx, cury = self.buttons['A']
        res = []
        for c in input_seq:
            if c == 'A':
                res.append(inv_buttons[(curx, cury)])
            elif c == '^':
                curx -= 1
            elif c == 'V':
                curx += 1
            elif c == '>':
                cury += 1
            elif c == '<':
                cury -=1
            if (curx, cury) not in self.buttons.values():
                print('Ooops')
                exit(1)
        return ''.join(res)

    def get_sequences(self, input_seq, current):
        if len(input_seq) == 0:
            yield("")
        else:
            curx, cury = self.buttons[current]
            x, y = self.buttons[input_seq[0]]
            dx = ''
            if x < curx:
                dx = '^' * (curx - x)
            elif x > curx:
                dx = 'V' * (x - curx)
            dy = ''
            if y < cury:
                dy = '<' * (cury - y)
            elif y > cury:
                dy = '>' * (y - cury)
            variants = set()
            if (x, cury) in self.buttons.values():
                variants.add(dx + dy + 'A')
            if (curx, y) in self.buttons.values():
                variants.add(dy + dx + 'A')
            for seq in self.get_sequences(input_seq[1:], input_seq[0]):
                for v in variants:
                    yield v + seq
    #         if 
    #     for c in input_seq:
    #         x, y = self.buttons[c]
            
    #         if x > curx:
    #             res += ['V'] * (x - curx)
    #         elif x < curx:
    #             res += ['^'] * (curx - x)
    #         if y > cury:
    #             res += ['>'] * (y - cury)
    #         elif y < cury:
    #             res += ['<'] * (cury - y)
    #         res += 'A'
    #         curx, cury = x, y
    #     return res
    

class NumKeyboard(BaseKeyboard):
    buttons = {'7': (0, 0), '8': (0, 1), '9': (0, 2),
               '4': (1, 0), '5': (1, 1), '6': (1, 2),
               '1': (2, 0), '2': (2, 1), '3': (2, 2),
               '0': (3, 1), 'A': (3, 2)}
                
class DirKeyboard(BaseKeyboard):
    buttons = {'^': (0, 1), 'A': (0, 2),
               '<': (1, 0), 'V': (1, 1), '>': (1, 2)}

    
res = 0
dir_kbd = DirKeyboard()
num_kbd = NumKeyboard()

seqs = set()
curseq = {''}
for _ in range(4):
    seqs.update(curseq)
    curseq = {x + y for x in curseq for y in '<>^V'}
    
blocks = {x + 'A': [seq + 'A' for seq in dir_kbd.get_sequence(x + 'A').split('A')[:-1]] 
          for x in seqs}
blocks['VA'] = ['V>A', '']

print(blocks)
for line in sys.stdin:
    numseq = line.strip()
    if len(numseq) == 0:
        break
    num_code = int(line[:3])
    seq0 =  list(num_kbd.get_sequences(numseq, 'A'))
    for s in seq0:
        #print(num_kbd.exec_sequence(s))
        assert num_kbd.exec_sequence(s) == numseq
    seq1 = []
    for x in seq0:
        sl = list(dir_kbd.get_sequences(x, 'A'))
        for s in sl:
            assert dir_kbd.exec_sequence(s) == x
        seq1.extend(list(dir_kbd.get_sequences(x, 'A')))
    #seq1 = [dir_kbd.get_sequence(x) for x in seq0]
    print('---------------')
    min_len = min(len(x) for x in seq1)
    print(num_code, seq0)
    #print(num_code, len([x for x in seq1 if len(x) == min_len]), len(seq1), min_len)
    #print(seq1)
    #print(num_code, min_len)
    seq2 = []
    min_len = None
    for x in seq1:
        parts = [block + 'A' for block in x.split('A')[:-1]]
        curcount = collections.Counter(parts)
        for step in range(STEPS):
            newcount = collections.Counter()
            for block in curcount:
                #newcount.update(blocks[block] * curcount[block])
                inner_counter = collections.Counter(blocks[block])
                #rint(block, inner_counter)
                for b, value in inner_counter.items():
                    newcount.update({b: curcount[block] * value})
            curcount = newcount
        cur_len = sum([len(block) * curcount[block] for block in curcount])
        if min_len is None or min_len > cur_len:
            min_len = cur_len
    res += num_code * (min_len or 0)
    print(num_code, min_len)
    #print(num_code, len([x for x in seq2 if len(x) == min_len]), len(seq2), min_len)
    #print(num_code, min_len)

print(res)

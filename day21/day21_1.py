import sys
#import itertools

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
            if y >= cury:
                res += ['>'] * (y - cury) + dx + ['A']
            else:
                res += dx + ['<'] * (cury - y) + ['A']
            curx, cury = x, y
        return res
                
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
        return res

            # if x > curx:
            #     res += ['V'] * (x - curx)
            # elif x < curx:
            #     res += ['^'] * (curx - x)
            # if y > cury:
            #     res += ['>'] * (y - cury)
            # elif y < cury:
            #     res += ['<'] * (cury - y)
            # res += 'A'


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
            # if len(variants) == 0:
            #     print(self.buttons, current, input_seq[0])
            #     exit(1)
            #variants = set((dx + dy + 'A', dy + dx + 'A'))
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

for line in sys.stdin:
    numseq = line.strip()
    if len(numseq) == 0:
        break
    num_code = int(line[:3])
    seq0 =  list(num_kbd.get_sequences(numseq, 'A'))
    seq1 = []
    for x in seq0:
        seq1.extend(list(dir_kbd.get_sequences(x, 'A')))
    seq2 = []
    for x in seq1:
        seq2.extend(list(dir_kbd.get_sequences(x, 'A')))
    min_len = min(len(x) for x in seq2)
    res += num_code * min_len
    #print([x for x in seq2 if len(x) == min_len])
    #print(num_code, min_len)

print(res)

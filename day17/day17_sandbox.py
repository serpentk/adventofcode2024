input()
input()
input()
input()
program = [int(x) for x in input().strip()[9:].split(',')]


def guess_start(a, program):
    b = program[-1]
    for r in range(8):
       cur_a = a * 8 + r 
       cur_b = (cur_a % 8) ^ 3 # 2 4, 1 3
       cur_c = cur_a // (2 ** cur_b) # 7 5
       cur_b = cur_c ^ cur_b # 4 2
       cur_b = (cur_b ^ 5) % 8 # 1 5
       if b == cur_b:
           if len(program) == 1:
               yield cur_a
           else:
               for x in guess_start(cur_a, program[:-1]):
                   yield x

print(min([x for x in guess_start(0, program)]))

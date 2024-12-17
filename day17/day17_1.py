
a = int(input().strip()[12:])
b = int(input().strip()[12:])
c = int(input().strip()[12:])
input()

def combo(x):
    if x <= 3:
        return x
    return {4: a, 5: b, 6: c}[x]
        

program = [int(x) for x in input().strip()[9:].split(',')]
out_val = []
pointer = 0
while True:
    try:
        cmd = program[pointer]
        print(cmd)
        if cmd == 0: # adv
            a = int(a / (2 ** combo(program[pointer + 1])))
            pointer += 2
        elif cmd == 1: # bxl
            b = b ^ program[pointer + 1]
            pointer += 2
        elif cmd == 2: # bst
            b = combo(program[pointer + 1]) % 8
            pointer += 2
        elif cmd == 3: # jnz
            if a == 0:
                pointer += 2
            else:
                pointer = program[pointer + 1]
        elif cmd == 4: # bxc
            b = b ^ c
            pointer += 2
        elif cmd == 5: # out
            out_val.append(combo(program[pointer + 1]) % 8)
            pointer += 2
        elif cmd == 6: # bdv
            b = int(a / 2 ** combo(program[pointer + 1]))
            pointer += 2
        elif cmd == 7: # cdv
            c = int(a / 2 ** combo(program[pointer + 1]))
            pointer += 2
    except Exception:
        break
print(','.join([str(x) for x in out_val]))

        
        

def simple_assembler(progogram):
    prog = progogram
    D = {}
    i = 0
    while i < len(prog):
        instruction = [str(x) for x in prog[i].split()]
        if instruction[0] == 'mov':
            if instruction[2] in D:
                D[instruction[1]] = D[instruction[2]]
            else:
                D[instruction[1]] = int(instruction[2])
            i += 1
        if instruction[0] == 'inc':
            D[instruction[1]] = int(D[instruction[1]]) + 1
            i += 1
        if instruction[0] == 'dec':
            D[instruction[1]] = int(D[instruction[1]]) - 1
            i += 1
        if instruction[0] == 'jnz':
            if instruction[1] in D:
                if D[instruction[1]] != 0:
                    i += int(instruction[2])
                else:
                    i += 1
            if instruction[1] == '0':
                i += 1
            if instruction[1] not in D and instruction[1] != '0':
                i += int(instruction[2])
        
    return D


code = ['mov a 5', 'inc a', 'dec a', 'dec a', 'jnz a -1', 'inc a']

print(simple_assembler(code))

code = ['mov a -10','mov b a','inc a','dec b','jnz a -2']

print(simple_assembler(code))

code = '''\
mov c 12
mov b 0
mov a 200
dec a
inc b
jnz a -2
dec c
mov a b
jnz c -5
jnz 0 1
mov c a'''

print(simple_assembler(code.splitlines()))







#Test.assert_equals(simple_assembler(code.splitlines()), {'a': 1})


#Test.assert_equals(simple_assembler(code.splitlines()), {'a': 409600, 'c': 409600, 'b': 409600})

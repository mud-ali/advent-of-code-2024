filename = 'input.txt'
# comment out to run on real input
# filename = 'test.txt'

stdout=[]
ip = 0
with open(filename, 'r') as file:
    lines = file.read().split("\n")
    a,b,c,program = [line.split(': ')[1] for line in lines if line != '']
    a,b,c = int(a), int(b), int(c)
    program = [int(instruction) for instruction in program.split(",")]
    
    def combo_operand(op) -> int:
        if op in [0,1,2,3]: return op
        match op:
            case 4:
                return a
            case 5:
                return b
            case 6:
                return c
        
    def opcode(name, operand):
        global a,b,c
        match name:
            case 0:
                a = a // (2 ** combo_operand(operand))
            case 1:
                b = b ^ operand
            case 2:
                b = combo_operand(operand) % 8
            case 3:
                if a != 0:
                    global ip
                    ip = operand - 2
            case 4:
                b ^= c
            case 5:
                stdout.append(str(combo_operand(operand) % 8))
            case 6:
                b = a // (2 ** combo_operand(operand))
            case 7:
                c = a // (2 ** combo_operand(operand))
            
            
    
    while ip < len(program):
        opcode(program[ip], program[ip+1])
        ip += 2
    print(",".join(stdout))
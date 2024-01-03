import json
from collections import defaultdict

instrucetion, INPUT = '', ''
FUNC_MP, ADDR_LIST, SICXE_LINE, RESULT = defaultdict(str), [], [], []
startFlag = True

REGISTER_LIST = {
    'A':['0', '0'], # [number, address]
    'X':['1', '0'],
    'L':['2', '0'],
    'B':['3', '0'],
    'S':['4', '0'],
    'T':['5', '0'],
    'F':['6', '0'],
    'PC':['8', '0'],
    'SW':['9', '0']
}

def isComment(line: str) -> bool:
    return line[0] == '.'

def BYTE(line: str) -> list:
    mode, data = line[0], line[2:-1]
    obj = ''

    if mode == 'C':
        obj += ''.join([hex(ord(c))[2:] for c in data])
    elif mode == 'X':
        obj += data
    else:
        return 0, 'ERROR'
    
    return len(obj) // 2, obj

def WORD(line: str) -> list:
    value, obj = int(line), ''

    if value >= 0:
        obj = hex(value)[2:]
    else:
        obj = hex(int('1000000', 16) + value)[2:]

    return len(obj) // 2, obj

def RESB(line: str) -> int:
    return int(line)

def RESW(line: str) -> int:
    return int(line) * 3

def setLocation() -> None:
    global SICXE_LINE, startFlag, ADDR_LIST, FUNC_MP, RESULT
    
    for line in INPUT:
        line = line.strip().split()

        if isComment(line):
            print('is Comment!!!')
            continue

        SICXE_LINE.append(line)

    if SICXE_LINE[0][1] != 'START':
        print('START ERROR ! ! !')
        startFlag = False

        return

    RESULT.append(['5', hex(int(SICXE_LINE[0][2]))[2:].zfill(4), SICXE_LINE[0][0], SICXE_LINE[0][1], SICXE_LINE[0][2], ''])

    next_ADDR = int(SICXE_LINE[0][2], 16)

    for i, line in enumerate(SICXE_LINE):
        if i == 0: continue

        cur_ADDR, FIRST, SECOND, THIRD, OBJ = next_ADDR, '', '', '', ''

        if len(line) == 1:
            SECOND = line[-1]
            OBJ = hex(int(instrucetion['instrucetion'][line[-1]][0], 16) + 3)[2:] + '0000'

        elif len(line) >= 2:
            if len(line) == 3:
                FIRST = line[-3]
                FUNC_MP[FIRST] = hex(cur_ADDR)[2:].zfill(4)

            SECOND = line[-2]
            THIRD = line[-1]
        
        ADDR_add = 0

        if SECOND[0] == '+':
            next_ADDR += 4
        elif SECOND not in instrucetion['pseudo']:
            next_ADDR = cur_ADDR + int(instrucetion['instrucetion'][SECOND][1])
        else:
            if SECOND == 'BYTE':
                ADDR_add, OBJ = BYTE(line[-1])
            elif SECOND == 'WORD':
                ADDR_add, OBJ = WORD(line[-1])
            elif SECOND == 'RESB':
                ADDR_add = RESB(line[-1])
            elif SECOND == 'RESW':
                ADDR_add = RESW(line[-1])
            elif SECOND == 'BASE':
                REGISTER_LIST['B'][1] = line[-1] if 'A' <= line[-1][0] <= 'Z' else line[-1][1:]

            next_ADDR = cur_ADDR + ADDR_add

        ADDR_LIST.append(f'{hex(cur_ADDR)[2:].zfill(4)}')
        RESULT.append([f'{i * 5 + 10}', hex(cur_ADDR)[2:].zfill(4), FIRST, SECOND, THIRD, OBJ])

def objCode() -> None:
    global REGISTER_LIST, RESULT

    for idx, info in enumerate(RESULT):
        if info[3] in instrucetion['pseudo'] or len(info[-1]) > 0:
            continue

        tmp = info.copy()

        if instrucetion['instrucetion'][tmp[3].replace('+', '')][1] == '2':
            if tmp[3].replace('+', '') == 'clear':
                REGISTER_LIST[tmp[-2]] = '0'

            R_list = tmp[-2].split(',')

            if len(R_list) == 1:
                RESULT[idx][-1] = f"{instrucetion['instrucetion'][tmp[3].replace('+', '')][0]}{REGISTER_LIST[R_list[0]][0]}0"
            else:
                RESULT[idx][-1] = f"{instrucetion['instrucetion'][tmp[3].replace('+', '')][0]}{REGISTER_LIST[R_list[0]][0]}{REGISTER_LIST[R_list[1]][0]}"
        else:
            n, i, x, b, p, e = 0, 0, 0, 0, 0, 0

            if tmp[-2][0] == '#':
                i = 1
                tmp[-2] = tmp[-2][1:]
            elif tmp[-2][0] == '@':
                n = 1
                tmp[-2] = tmp[-2][1:]
            else:
                n, i = 1, 1

            if ',X' in tmp[-2]:
                x = 1
                tmp[-2] = tmp[-2].split(',')[0]

            if tmp[3][0] == '+':
                e = 1
                tmp[3] = tmp[3][1:]

            obj = hex(int(instrucetion['instrucetion'][tmp[3]][0], 16) + int(f'{n}{i}', 2))[2:].zfill(2)

            if e == 1:
                obj += hex(int(f'{x}{b}{p}{e}', 2))[2:]

                if n == 0 and i == 1 and tmp[-2].lstrip('-').isdigit():
                    if int(tmp[-2]) < 0:
                        obj += hex(int(tmp[-2]) + int('1000', 16))[2:].zfill(5)
                    else:
                        obj += hex(int(tmp[-2]))[2:].zfill(5)
                else:
                    obj += FUNC_MP[tmp[-2]].zfill(5)
            else:
                disp = ''
                if n == 0 and i == 1 and tmp[-2].lstrip('-').isdigit():
                    if int(tmp[-2]) < 0:
                        disp += hex(int(tmp[-2]) + int('1000', 16))[2:]
                    else:
                        disp += hex(int(tmp[-2]))[2:]
                else:
                    disp = int(FUNC_MP[tmp[-2]], 16) - int(ADDR_LIST[ADDR_LIST.index(tmp[1]) + 1], 16)

                    if x == 1:
                        disp -= int(REGISTER_LIST['X'][1], 16)

                    if disp < -2048 or 2047 < disp:
                        b = 1

                        disp = int(FUNC_MP[tmp[-2]], 16) - int(FUNC_MP[REGISTER_LIST['B'][1]], 16)

                        if x == 1:
                            disp -= int(REGISTER_LIST['X'][1], 16)
                    else:
                        p = 1

                    if disp < 0:
                        disp = hex(disp + int('1000', 16))[2:]
                    else:
                        disp = hex(disp)[2:]

                obj += f"{hex(int(f'{x}{b}{p}{e}', 2))[2:]}{disp.zfill(3)}"

            RESULT[idx][-1] = obj

def SICXE_Assambler() -> None:
    print('SICXE_Assambler')

    setLocation()

    print('\n'.join(ADDR_LIST))

    objCode()

    if not startFlag:
        return
    
    for line in RESULT:
        print(line)

    

if __name__ == '__main__':
    print('test')

    with open('INPUT.txt', 'r', encoding='UTF-8') as inp:
        INPUT = inp.readlines()

    print(INPUT)

    with open('instrucetion_SICXE.json', 'r', encoding='UTF-8') as inp:
        instrucetion = json.load(inp)

    print(instrucetion)

    SICXE_Assambler()

    with open('OUTPUT.txt', 'w', encoding='UTF-8') as outp:
        for line in RESULT:
            if len(line[3]) > 0 and len(line[-2]) > 0 and line[3][0] == '+' and line[-2][0] in ['#', '@']:
                outp.write(f'{line[0]:>5}     {line[1].upper()}        {line[2]:<8}    {line[3]:<6}     {line[-2]:<10}        {line[-1].upper()}')
            elif len(line[3]) > 0 and line[3][0] == '+':
                outp.write(f'{line[0]:>5}     {line[1].upper()}        {line[2]:<8}    {line[3]:<6}      {line[-2]:<9}        {line[-1].upper()}')
            elif len(line[-2]) > 0 and line[-2][0] in ['#', '@']:
                outp.write(f'{line[0]:>5}     {line[1].upper()}        {line[2]:<8}     {line[3]:<5}     {line[-2]:<10}        {line[-1].upper()}')
            else:
                outp.write(f'{line[0]:>5}     {line[1].upper()}        {line[2]:<8}     {line[3]:<5}      {line[-2]:<9}        {line[-1].upper()}')

            outp.write('\n')
    
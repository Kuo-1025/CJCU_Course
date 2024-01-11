def isComment(line: str) -> bool:
    return line[0] == '.' or len(line) == 0

with open('INPUT.txt', 'r', encoding='UTF-8') as f:
    inp = f.readlines()

    tmp = inp[0].strip().split()
    mainFn = [['5', tmp[0], tmp[1], tmp[2]]]

    SAVE, isMACRO = {}, ''
    LOC = 5

    for line in inp[1:]:
        FST, SND, THD = '', '', ''
        LOC += 5

        if isComment(line):
            continue

        line = line.strip().split()
        if len(line) == 1:
            SND = line[-1]
        elif len(line) == 2:
            SND, THD = line[-2], line[-1]
        elif len(line) == 3:
            FST, SND, THD = line[0], line[1], line[2]

        if SND == 'MACRO':
            isMACRO = FST
            SAVE[FST] = [THD.split(','), []]

            continue
        elif SND == 'MEND':
            isMACRO = ''

            continue

        if len(isMACRO) > 0:
            SAVE[isMACRO][1].append([LOC, FST, SND, THD])
        else:
            if SND in SAVE:
                cur = FST

                if cur != '':
                    FST = f'.{FST}'

                mainFn.append([str(LOC), FST, SND, THD])

                elem = {}
                THD = THD.split(',')

                for idx, para in enumerate(SAVE[SND][0]):
                    elem[para] = THD[idx]

                SAVE[SND][1][0][1] = cur

                for idx, line1 in enumerate(SAVE[SND][1]):
                    cur_line = line1.copy()

                    cur_line[0] = str(LOC) + chr(ord('a') + idx)
                    for i in elem:
                        if i in cur_line[3]:
                            cur_line[3] = cur_line[3].replace(i, elem[i])

                    mainFn.append(cur_line.copy())

            else:
                mainFn.append([str(LOC), FST, SND, THD])

for i in mainFn:
    print(i)
with open('OUTPUT.txt', 'w', encoding='UTF-8') as f:
    for line in mainFn:
        loc_split = []
        if ord(line[0][-1]) < ord('0') or ord('9') < ord(line[0][-1]):
            loc_split.append(line[0][:-1])
            loc_split.append(line[0][-1])
        else:
            loc_split.append(line[0])

        if len(loc_split) == 1:
            f.write(f'{loc_split[0]:>3}      ')
        else:
            f.write(f'{loc_split[0]}{loc_split[1]:}     ')
        
        ######################################################################################################

        f.write(f'{line[1]:<8}')
        f.write('   ' if len(line[2]) > 0 and line[2][0] == '+' else '    ')
        
        ######################################################################################################
            
        if len(line[2]) > 0 and line[2][0] == '+':
            f.write('+')
            line[2] = line[2][1:]
        f.write(f'{line[2]:<8}')
        f.write('    ' if len(line[3]) > 0 and line[3][0] in ['#', '@', '='] else '     ')

        ######################################################################################################

        f.write(f'{line[3]}')
        f.write('\n')
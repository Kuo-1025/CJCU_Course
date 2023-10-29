import SIC_Instruction
from collections import defaultdict

def comment(line: str) -> list:
    for i in range(len(line)):
        if line[i].find('.') != -1:
            return line[:i]
        
    return line

def BYTE(thrd: str) -> list:
    mode, data = thrd[0], ""

    if mode == "C":
        data += ''.join([hex(ord(c))[2:] for c in thrd[2:-1]]).upper()

    elif mode == "X":
        data += thrd[2:-1]

    else:
        print("ERROR BYTE OAO")

    return len(data) // 2, data

def WORD(thrd: str) -> list:
    value, data = int(thrd), ""

    if value >= 0:
        data = hex(value)[2:].upper().zfill(6)

    else:
        HEX = "1000000"
        data = hex(int(HEX, 16) + value)[2:].upper().zfill(6)

    return len(data) // 2, data

def RESB(thrd: str) -> list:
    return int(thrd), ""

def RESW(thrd: str) -> list:
    return int(thrd) * 3, ""

def Assambler() -> None:
    EMPTY = ""
    LOCATION, ADD = 0, 0
    RESULT, FUNC_LOC = [], defaultdict(int)

    with open("INPUT.txt", "r", encoding="UTF-8") as inp:
        SIC = inp.readlines()

        for line in SIC:
            line = comment(line.strip().split())
            fst, snd, thrd, objCode = "", "", "", ""

            if len(line) == 0:
                continue

            if LOCATION == 0:
                if line[-2] != "START":
                    print("ERROR START OAO")
                    exit()

                LOCATION = int(line[-1], 16)
                fst, snd, thrd = line[0], line[1], line[2]

                RESULT.append(["", fst, snd, thrd, objCode])

                continue

            else:
                if len(line) == 1:
                    snd = line[0]
                    objCode = SIC_Instruction.instruction[snd] + "0000"

                else:
                    snd = line[0] if len(line) == 2 else line[1]

                    if snd in SIC_Instruction.instruction:
                        thrd = line[-1]
                        ADD = 3

                        if len(line) == 3:
                            fst = line[0]
                            FUNC_LOC[fst] = LOCATION

                    else:
                        if snd == "END":
                            ADD = 0
                            thrd = line[-1]

                        else:
                            fst, snd, thrd = line[0], line[1], line[2]
                            FUNC_LOC[fst] = LOCATION

                            if snd == "BYTE":
                                ADD, objCode = BYTE(thrd)
                            elif snd == "WORD":
                                ADD, objCode = WORD(thrd)
                            elif snd == "RESB":
                                ADD, objCode = RESB(thrd)
                            elif snd == "RESW":
                                ADD, objCode = RESW(thrd)

            RESULT.append([hex(LOCATION)[2:].upper(), fst, snd, thrd, objCode])
            LOCATION += ADD

        for idx in range(len(RESULT)):
            if RESULT[idx][0] == "": continue

            elif RESULT[idx][2] in ["END", "BYTE", "WORD", "RESB", "RESW"]: continue

            else:
                if len(RESULT[idx][4]) == 0:
                    if ",X" in RESULT[idx][3]:
                        RESULT[idx][4] = SIC_Instruction.instruction[RESULT[idx][2]] + hex(FUNC_LOC[RESULT[idx][3]] + int("8000", 16))[2:].upper().zfill(4)
                    else:
                        RESULT[idx][4] = SIC_Instruction.instruction[RESULT[idx][2]] + hex(FUNC_LOC[RESULT[idx][3]])[2:].upper()

        for res in RESULT:
            for s in res:
                print(f"{s:<10}", end="")

            print()

    with open("OUTPUT.txt", "w", encoding="UTF-8") as fi:
        for i in range(len(RESULT)):
            fi.write(f"{(i + 1) * 5:<10}{RESULT[i][0]:<10}{RESULT[i][1]:<10}{RESULT[i][2]:<10}{RESULT[i][3]:<10}{RESULT[i][4]:<10}\n")
 
    return

Assambler()
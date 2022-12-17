from GeneralTools import decimalToBinary
from GeneralTools import binaryToDecimal
from GeneralTools import pcOff9
from GeneralTools import twosCom_binDec

def BinaryToLC3():
    fullCom = input('Please enter your binary command: ')
    ins = int(str(fullCom)[:4])
    ins: int = binaryToDecimal(ins)

    # Add instruction
    if ins == 1:
        print("ADD", end=' ')
        print("R" + str(binaryToDecimal(int(str(fullCom)[4:7]))), end=' ')
        print("R" + str(binaryToDecimal(int(str(fullCom)[7:10]))), end=' ')

        if int(str(fullCom)[10:11]) == 0:
            print("R" + str(binaryToDecimal(int(str(fullCom)[13:16]))))

        elif int(str(fullCom)[10:11]) == 1:
            print("#" + str(twosCom_binDec(fullCom[11:16], 5)))

    elif ins == 2:
        print("LD", end=' ')
        # Still need to do twos complement
        print("R" + str(binaryToDecimal(int(str(fullCom)[4:7]))), end=' ')
        print("#" + str(twosCom_binDec(fullCom[8:16], 9)))

    elif ins == 3:
        print("ST", end=' ')
        # Still need to do twos complement
        print("R" + str(binaryToDecimal(int(str(fullCom)[4:7]))), end=' ')
        print("#" + str(twosCom_binDec(fullCom[8:16], 9)))

    elif ins == 4:
        print("NOT DONE", end=' ')

    elif ins == 5:
        print("AND", end=' ')
        print("R" + str(binaryToDecimal(int(str(fullCom)[4:7]))), end=' ')
        print("R" + str(binaryToDecimal(int(str(fullCom)[7:10]))), end=' ')

        if int(str(fullCom)[10:11]) == 0:
            print("R" + str(binaryToDecimal(int(str(fullCom)[13:16]))))

        elif int(str(fullCom)[10:11]) == 1:
            print(" " + fullCom[11:16])

    elif ins == 6:
        print("LDR", end=' ')
        # Still need to do twos complement
        print("R" + str(binaryToDecimal(int(str(fullCom)[4:7]))), end=' ')
        print("R" + str(binaryToDecimal(int(str(fullCom)[7:10]))), end=' ')
        print("#" + str(twosCom_binDec(fullCom[10:16], 6)))

    elif ins == 7:
        print("STR", end=' ')
        # Still need to do twos complement
        print("R" + str(binaryToDecimal(int(str(fullCom)[4:7]))), end=' ')
        print("R" + str(binaryToDecimal(int(str(fullCom)[7:10]))), end=' ')
        print("#" + str(twosCom_binDec(fullCom[10:16], 6)))

    elif ins == 8:
        print("RTI")

    elif ins == 9:
        print("NOT", end=' ')
        print("R" + str(binaryToDecimal(int(str(fullCom)[4:7]))), end=' ')
        print("R" + str(binaryToDecimal(int(str(fullCom)[7:10]))), end=' ')

    elif ins == 10:
        print("LDI", end='')
        print("R" + str(binaryToDecimal(int(str(fullCom)[4:7]))), end=' ')
        print("#" + str(twosCom_binDec(fullCom[8:16], 9)))

    elif ins == 11:
        print("STI", end='')
        print("R" + str(binaryToDecimal(int(str(fullCom)[4:7]))), end=' ')
        print("#" + str(twosCom_binDec(fullCom[8:16], 9)))

    elif ins == 12:
        print("RET")

    elif ins == 13:
        print("Reserved")

    elif ins == 14:
        print("LEA", end=' ')
        print("R" + str(binaryToDecimal(int(str(fullCom)[4:7]))), end=' ')
        print("#" + str(twosCom_binDec(fullCom[8:16], 9)))

    elif ins == 15:
        print("TRAP", end=' ')
        print(binaryToDecimal(fullCom[9:16]))

    print("\n1. for binary to LC3 again")
    print("2. To Go up a menu")
    nexCom: int = int(input('Enter your choice: '))

    if nexCom == 1:
        BinaryToLC3()

    else:
        printCompArch()


def printCompArch():
    print("1. -- Convert binary to LC3 instruction --")

    subChoice = input('Please enter your subject: ')

    if subChoice == '1':
        print("Convert binary to LC3")
        BinaryToLC3()

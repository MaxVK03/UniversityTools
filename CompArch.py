from GeneralTools import decimalToBinary
from GeneralTools import binaryToDecimal


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
            print("#" + str(binaryToDecimal(int(str(fullCom)[11:16]))))

    elif ins == 2:
        print("LD")
        print("R" + str(binaryToDecimal(int(str(fullCom)[4:7]))), end=' ')
        print("#" + str(binaryToDecimal(int(str(fullCom)[7:16]))))

    print("1. for binary to LC3 again")
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

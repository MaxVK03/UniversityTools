from GeneralTools import binaryToDecimal
from GeneralTools import twosCom_binDec
from GeneralTools import hexToDec
from DB_Manager import getCompArch

def BinaryToLC3(binNumIn, Typex):
    fullCom: str = binNumIn
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

    elif ins == 0:
        print("BR", end='')
        if fullCom[4:5] == '1':
            print("N", end='')

        if fullCom[5:6] == '1':
            print("Z", end='')

        if fullCom[6:7] == '1':
            print("P", end='')

        print(" #" + str(twosCom_binDec(fullCom[7:16], 9)))

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
            print("#" + str(binaryToDecimal(int(str(fullCom[11:16])))))

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
        print("LDI ", end='')
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
        print("TRAP Please check code x25 means halt")
        #print(binaryToDecimal(fullCom[9:15]))

    if Typex == "Bin":
        print("\n1. for binary to LC3 again")
        print("2. To Go up a menu")
        nexCom: int = int(input('Enter your choice: '))

        if nexCom == 1:
            fullCom = input('Please enter your binary command: ')
            BinaryToLC3(fullCom, 'Bin')
        else:
            printCompArch()

    if Typex == "Hex":
        print("\n1. for hex to LC3 again")
        print("2. To Go up a menu")
        nexCom: int = int(input('Enter your choice: '))

        if nexCom == 1:
            HexToLC3()
        else:
            printCompArch()


def HexToLC3(hexIns):
    type = 'conHex'
    if len(hexIns) < 1:
        fullCom = input('Please enter your hex command: ')
        type = 'Hex'
    else:
        fullCom = hexIns
    binIns = format(int(fullCom, 16), "016b")
    BinaryToLC3(binIns, type)

def getLC3Comm():
    Commands = getCompArch()

    for i, comms in enumerate(Commands):
        print(str(i+1) + ". " + str(comms[1]))

    LC3commChoice = input("Enter which command you would like: ")
    print()
    if(int(LC3commChoice) <= len(Commands[1])):
        print(Commands[int(LC3commChoice)-1][2] + "\n")

    else:
        print("Invalid command")

def printCompArch():
    print("1. -- Convert full bin to LC3 instruction Not Complete --")
    print("2. -- Convert full Hex to LC3 instruction --")
    print("3. -- Get LC3 code snippets --")
    subChoice = input('\nPlease enter your chosen application: ')


    if subChoice == '1':
        print("Enter in your instructions press xxxx to exit")
        subChoice = input('')
        if(subChoice == 'xxxx'):
            printCompArch()
        inps = []
        while subChoice != 'xxxx':
            inps.append(subChoice)
            subChoice = input('')

        for i in subChoice:
            BinaryToLC3(i, 'conBin')

        printCompArch()

    if subChoice == '2':
        print("Enter your commands and press xxxx when finished")
        cou = 1
        subChoice = input()
        inps = []
        reachHalt = False
        while subChoice != 'xxxx':
            inps.append(subChoice)
            subChoice = input()
            cou += 1

        for i in inps:
            inp = i.replace('x', "")


            if len(inp) == 4:
                print(inp + " ", end=' ')

                try:
                    if(not reachHalt):
                        HexToLC3(inp)
                    else:
                        print("x" + str(inp))
                except ValueError:
                    print("Please check your commands. It seems there is a error")

                if(inp[0:1] == 'F'):
                    if inp[2:4] == '25':
                        reachHalt = True

    if subChoice == '3':
        getLC3Comm()

    printCompArch()

#print("Doing this")
#printCompArch()

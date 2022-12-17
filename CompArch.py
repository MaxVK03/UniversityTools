from GeneralTools import decimalToBinary

def BinaryToLC3():
    print("enter your number")
    fullCom = input('Please enter your subject: ')
    ins = int(str(fullCom)[:4])
    print(ins)
    print()



def printCompArch():
    print("1. Convert binary to LC3 instruction")

    subChoice = input('Please enter your subject: ')

    if subChoice == 1:
        print("Convert binary to LC3")

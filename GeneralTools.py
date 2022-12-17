def decimalToBinary(n):
    return bin(n).replace("0b", "")


def binaryToDecimal(binary):
    decimal, i = 0, 0
    while binary != 0:
        dec = binary % 10
        decimal = decimal + dec * pow(2, i)
        binary = binary // 10
        i += 1
    return decimal


def pcOff9(binnum):
    numChe = str(binnum)[8:16]


def pcOff5(binnum):
    binStr = str(binnum)
    if binStr[8:9] == '0':
        return binaryToDecimal(binnum)

    elif binStr[8:9] == '1':
        addNeg = int(binStr[9:16])
        return -265 + addNeg

def twosCom_binDec(bin, digit):
    while len(bin) < digit:
        bin = '0' + bin
    if bin[0] == '0':
        return int(bin, 2)
    else:
        return -1 * (int(''.join('1' if x == '0' else '0' for x in bin), 2) + 1)

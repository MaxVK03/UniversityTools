from CompArch import printCompArch


def printMenu():
    print("Select a subject")
    print("1. -- Computer Architecture --")
    print("2. -- Discrete Structures --")
    subChoice = input('\n Please enter your subject: ')

    if subChoice == '1':
        printCompArch()

from CompArch import printCompArch


def printMenu():
    print("Select a subject")
    print("1. -- Computer Architecture --")
    print("2. -- Discrete Structures -- TBA")
    print("3. -- Imperative programming -- TBA")
    subChoice = input('\n Please enter your subject: ')

    if subChoice == '1':
        printCompArch()

from CompArch import printCompArch


def printMenu():
    print("Select a subject")
    print("1 Computer Architecture")

    subChoice = input('Please enter your subject: ')

    if subChoice == '1':
        printCompArch()

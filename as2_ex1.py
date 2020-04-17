import os
import copy
running = True

# Sort array by sallary
def sortOtion(element):
    helper=element[2]
    return int(helper.replace(",",""))

# Print Array in table form
def printArray(data):
    for i in range(len(data)):
        for j in range(len(data[i])):
            print(data [i][j], end='|')
        print(" ")

# Change order of Array into the given 
def ChangeOrder(data):
    counter = -1

    for line in data:
            counter += 1
            changeOrder = []
            changeV = line[3]
            changeOrder.append(changeV)
            changeV = line[2]
            changeOrder.append(changeV)
            changeV = line[4]
            changeOrder.append(changeV)
            changeV = line[1]
            changeOrder.append(changeV)
            changeV = line[0]
            changeOrder.append(changeV)
            data[counter] = changeOrder
    return data

# Normilize table into 15 and 8 character
def StandartForm(data):
    for line in data:
            counter = -1
            for word in line:
                counter += 1
                AddSpacesNumber = 15 - len(line[counter])
                if counter == 2:
                    zeroSpace = 0
                    for char in line[counter]:
                        if char == ",":
                            zeroSpace += 1

                    AddSpacesNumber = 8 - len(line[counter]) + zeroSpace

                if AddSpacesNumber < 0: 
                    print("smaler")
                line[counter] = line[counter] + (" " * AddSpacesNumber)


# Searech by surname
def lastName(data):
    surname = str(input("1) Enter name for searech: "))
    result = []
    counter = 0
    for line in data:
        if line[0] == surname:
             print("Result is ")
             result.append(line)
    StandartForm(result)
    printArray(result)
# searech by team nam
def team(data):
    teamName = str(input("1) Enter name of team for searech: "))
    result = []
    counter = 0
    for line in data:
        if line[4] == teamName:
             print("Result is ")
             result.append(line)
    StandartForm(result)
    printArray(result)
# searech by Salary Range
def salaryRange(data):
    lower = int(input("1) Enter lower boundary for salary: "))
    upper = int(input("2) Enter upper boundary for salary: "))
    os.system('cls')
    sortArr =[]
    validator = False
    print("Result is: ")
    result = ()
    counter = 0

    for line in data:
        if lower > upper:
            break

        number = line[2]
        newNumber = ''

        for letter in number:
            if letter != ',':
                newNumber = newNumber + letter
        newNumber = int(newNumber)
        if lower < newNumber < upper:
            sortArr.append(line)
            validator = True
    if validator == False:
        print("Nd data found")
    else:
        sortArr.sort(key=sortOtion)
        StandartForm(sortArr)
        printArray(sortArr)

    
# Main part
def WorkFile(fileName):
    print("")
    data = []
    dataForSearech = []
    cwd = os.getcwd()


    fullPath = cwd + '/' + fileName
    try: 
        fileW = open(fullPath, 'r')
        for line in fileW:
            element = line.split()
            data.append(element)
        # Show initial Array from file
        print("Initial Data (In a file)")
        print("                      ")
        printArray(data)
        print("******************************************************")

        # Show array after changing order
        ChangeOrder(data)
        
        print("Data after changing order")
        print("                      ")
        OldData = copy.deepcopy(data)
        printArray(data)
        print("******************************************************")
        # Show Array after normalizationn process
        StandartForm(data)
        
        print("Data after 15 and 8 character normalization process")
        print("                      ")
        printArray(data)
        print("******************************************************")

        print("Searech Options: ")
        print("1) Enter 1 to searech by surname")
        print("2) Enter 2 to searech by Salary Range")
        print("3) Enter 3 to searech by team name")
        print("4) Enter 4 to go to the beginning of program")

        options = int(input("Enter searech option: "))
        # Choice option
        if options == 1:
            os.system('cls')
            lastName(OldData)
        if options == 2:
            os.system('cls')
            print("Searech by salary starts")
            salaryRange(OldData)
        if options == 3:
            team(OldData)
        if options == 4:
            return
        else:
            print("Incorrect option")
            


    except:
        print("File reading failed. Try to change starting directory or see if fail is exist")

# **************** Start of program *********************
while running:
    print("1) Enter 1 to start program")
    print("2) Enter 2 to exist from program")
    number = int(input("Enter option of work: "))
    if number == 1: 
        os.system('cls')
        fileName = input("Enter file name: ")
        os.system('cls')
        WorkFile(fileName)
    if number == 2:
        running =  False
    else:
        print("Incorrect option")
else:
    print("Program ends")

# **************** End of program loop *********************
